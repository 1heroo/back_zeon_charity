# Generated by Django 4.1.1 on 2022-10-10 22:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_alter_donations_payment_dt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donations',
            name='payment_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 11, 4, 2, 6, 995130), null=True, verbose_name='payment_dt'),
        ),
        migrations.AlterField(
            model_name='wallettransactions',
            name='payment_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 11, 4, 2, 6, 995299), null=True, verbose_name='payment_dt'),
        ),
    ]