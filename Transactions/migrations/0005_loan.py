# Generated by Django 5.1.2 on 2024-11-20 14:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Transactions', '0004_transaction_after_transaction_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('transaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Transactions.transaction')),
                ('purpose', models.CharField(max_length=50)),
                ('priority', models.CharField(max_length=50)),
                ('repayment_frequency', models.CharField(max_length=50)),
            ],
            bases=('Transactions.transaction',),
        ),
    ]
