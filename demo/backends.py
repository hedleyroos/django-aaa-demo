from mozilla_django_oidc.auth import OIDCAuthenticationBackend


class MyOIDCAB(OIDCAuthenticationBackend):

    def create_user(self, claims):
        user = super(MyOIDCAB, self).create_user(claims)

        #user.first_name = claims.get('given_name', '')
        #user.last_name = claims.get('family_name', '')
        #user.save()
        print(claims)
        return user

    def update_user(self, user, claims):
        #user.first_name = claims.get('given_name', '')
        #user.last_name = claims.get('family_name', '')
        #user.save()
        print(claims)
        return user


#@permission(domain, user_id, "urn:updb:product", "read")
#def get()
