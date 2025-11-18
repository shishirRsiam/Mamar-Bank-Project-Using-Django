#!/bin/bash

docker compose exec mamar_bank python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'shishir.siam01@gmail.com', 'admin')
    print('✅ Superuser created.')
else:
    print('⚠️  Superuser already exists.')
"