from mozilla_django_oidc.auth import OIDCAuthenticationBackend

from demo.models import UserProfile, Domain


class MyOIDCAB(OIDCAuthenticationBackend):

    def create_user(self, claims):
        user = super().create_user(claims)
        return user

    def update_user(self, user, claims):
        user = super().update_user(user, claims)
        try:
            profile = user.userprofile
        except UserProfile.DoesNotExist:
            profile = UserProfile.objects.create(user=user)
        profile.domain_access = claims["domain_access"]
        profile.save()
        for domain_name in claims["domain_access"].keys():
            domain, created = Domain.objects.get_or_create(name=domain_name)
        return user

    def has_perm(self, user, perm, *args, **kwargs):
        """If the user has the resource in his current domain then return True, else False.
        """

        # Alias
        profile = user.userprofile

        # A domain is required
        if not profile.current_domain:
            return False

        # Check permissions for current domain. The resources and permissions have a naming
        # convention.
        current_domain_name = profile.current_domain.name
        resource_permissions = profile.domain_access.get(current_domain_name, {}).get("resource_permissions", {})
        model_name, permission = perm.split(":")
        resource = "urn:updb:%s" % model_name
        return permission in resource_permissions.get(resource, [])
