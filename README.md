Django AAA Demo
===============
**Demo authentication and RBAC against a AAA service.**

Usage
-----

Add to `/etc/hosts` on your host operating system:

    172.29.44.101 core-management-portal core-access-control core-user-data-store core-authentication-service core-management-layer

Start the virtual machine::

    vagrant up aaa --provider virtualbox

SSH into the virtual machine when it is ready:

    ssh root@172.29.44.101

Start the containers. Many things can go wrong here (eg. DockerHub may rate limit you),
so keep an eye on the output. If things break then read the source of gogo.sh::

    /vagrant/gogo.sh

Wait two minutes for some housekeeping tasks to complete.

Visit `http://core-management-portal` on your host operating system browser. Note http, *not* https. Click login,
and on the subsequent page sign in with `cobusc` and password `something`.

Manual steps. Sorry, this part isn't automated yet.

Go to `http://core-authentication-service/en/admin/oidc_provider/client/6/change/`. Add
`http://localhost:8000/oidc/callback/` to `Redirect URIs`. Add
`http://localhost:8000/` to `Post Logout Redirect URI`. Save.

http://core-authentication-service/en/admin/authentication_service/coreuser/f8c437c6-0196-11ec-8758-0242c0a8130b/change/
Set Girl Effect organisation. Save.

http://core-management-portal/#/roles
Add `product_manager`.

http://core-management-portal/#/resources
Add `urn:updb:product`.

http://core-management-portal/#/domainroles
Add `girl_effect_organisation`, `product_manager`.

http://core-management-portal/#/roleresourcepermissions
Add `product_manager`, `urn:updb:product`, `create`.

http://core-management-portal/#/userdomainroles
Add `cobusc`, `girl_effect_organisation`, `product_manager`.

Finally start Django on your host operating system::

    /ve/bin/python manage.py runserver 0.0.0.0:8000

Browse to `http://localhost:8000`, and log in. This performs an Oauth login, and
since your are already logged in as cobusc you only need to grant permissions.

