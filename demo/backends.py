from mozilla_django_oidc.auth import OIDCAuthenticationBackend

from demo.models import UserProfile


class MyOIDCAB(OIDCAuthenticationBackend):

    def create_user(self, claims):
        user = super().create_user(claims)
        return user

    def update_user(self, user, claims):
        #import pdb;pdb.set_trace()
        user = super().update_user(user, claims)
        try:
            profile = user.userprofile
        except UserProfile.DoesNotExist:
            profile = UserProfile.objects.create(user=user)
        profile.resource_permissions = claims["resource_permissions"]
        profile.save()
        return user


#@permission(domain, user_id, "urn:updb:product", "read")
#def get()
