Django AAA Demo
===============
**Demo authentication and RBAC against a AAA service .**

Usage
-----

Add to `/etc/hosts` on your host operating system:

    172.29.44.101 core-management-portal core-access-control core-user-data-store core-authentication-service core-management-layer

Start the virtual machine::

    vagrant up aaa --provider virtualbox

SSH into the virtual machine when it is ready:

    ssh root@172.29.44.101

Start the containers::

    ./gogo.sh

Wait two minutes for some housekeeping tasks to complete.

Visit `http://core-management-portal` on your host operating system browser. Note http, *not* https. Click login,
and on the subsequent page sign in with `cobusc` and password `something`.