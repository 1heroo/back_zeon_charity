# Generated by Django 4.1.1 on 2022-10-13 12:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(blank=True, null=True, verbose_name='user')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
<<<<<<< HEAD
                ('payment_dt', models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 13, 18, 2, 49, 47654), null=True, verbose_name='payment_dt')),
=======
                ('payment_dt', models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 13, 16, 45, 53, 930367), null=True, verbose_name='payment_dt')),
>>>>>>> 4d1e5a685dd4055b9d95ae209f49288f8ca08788
                ('payment_success', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Donation',
                'verbose_name_plural': 'Donations',
            },
        ),
        migrations.CreateModel(
            name='WalletTransactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
<<<<<<< HEAD
                ('payment_dt', models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 13, 18, 2, 49, 47654), null=True, verbose_name='payment_dt')),
=======
                ('payment_dt', models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 13, 16, 45, 53, 930524), null=True, verbose_name='payment_dt')),
>>>>>>> 4d1e5a685dd4055b9d95ae209f49288f8ca08788
                ('payment_success', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Wallet-Transaction',
                'verbose_name_plural': 'Wallet-Transactions',
            },
        ),
    ]
