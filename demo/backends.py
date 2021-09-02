from mozilla_django_oidc.auth import OIDCAuthenticationBackend

from demo.models import UserProfile, Domain


class MyOIDCAB(OIDCAuthenticationBackend):

    def create_user(self, claims):
        user = super().create_user(claims)
        return user

    def update_user(self, user, claims):
        import pdb;pdb.set_trace()
        user = super().update_user(user, claims)
        try:
            profile = user.userprofile
        except UserProfile.DoesNotExist:
            profile = UserProfile.objects.create(user=user)
        profile.resource_permissions = claims["resource_permissions"]
        profile.domain_roles = claims["domain_roles"]
        profile.save()
        for domain_name, roles in claims["domain_roles"].items():
            domain, created = Domain.objects.get_or_create(name=domain_name)
        return user

    def has_perm(self, user, perm, *args, **kwargs):
        #import pdb;pdb.set_trace()
        model_name, permission = perm.split(":")
        resource = "urn:updb:%s" % model_name
        return permission in user.userprofile.resource_permissions.get(resource, [])
        #if args:
        #    instance = args[0]
        #return False
