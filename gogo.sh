#!/bin/bash

# Prepare to prepare
apt-get install yarnpkg git-core build-essential python-virtualenv docker-compose vim net-tools
ln -s /usr/lib/nodejs/yarn/bin/yarn.js /usr/local/bin/yarn

# Send in the clones
git clone https://github.com/hedleyroos/core-general
git clone https://github.com/hedleyroos/core-authentication-service
git clone https://github.com/hedleyroos/core-access-control
git clone https://github.com/hedleyroos/core-user-data-store
git clone https://github.com/hedleyroos/core-management-layer
git clone https://github.com/hedleyroos/core-management-portal

# Spin a yarn
cd core-management-portal
make build-virtualenv
rm -rf admin/generated/ node_modules/ yarn.lock
cd admin
yarn
cd ..
make generate-admin-headless

# Start the services
cd ~/core-general && make docker-network && make build-run-core

# Magic incantations in a specific order. We happen to know 7 will work when bootstrapping from scratch.
docker exec -ti compose_files_core-access-control_1 python seed_data.py
docker exec -ti compose_files_core-access-control_1 python bootstrap_management_portal.py 7

docker exec -ti compose_files_core-authentication-service_1  python manage.py demo_content
docker exec -ti compose_files_core-authentication-service_1 python manage.py shell -c "from authentication_service.models import CoreUser; CoreUser.objects.create_superuser(username='cobusc', email='cobusc@praekeltconsulting.com', password='something', birth_date='1979-01-13', pk='f8c437c6-0196-11ec-8758-0242c0a8130b')"
docker exec -ti compose_files_core-authentication-service_1 python manage.py creatersakey

docker exec -ti compose_files_core-access-control_1 python bootstrap_tech_admin_user.py  f8c437c6-0196-11ec-8758-0242c0a8130b
