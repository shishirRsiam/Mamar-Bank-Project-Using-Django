# Generated by Django 5.1.2 on 2024-11-20 15:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Transactions', '0006_alter_transaction_after_transaction_balance'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='approve_admin',
            field=models.ForeignKey(null=1, on_delete=django.db.models.deletion.CASCADE, related_name='approved_admin', to=settings.AUTH_USER_MODEL),
            preserve_default=1,
        ),
    ]
