# Generated by Django 4.1.1 on 2022-10-06 03:58

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cards', '0004_volunteer_remove_donations_user_id_donations_region_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='phone_number',
            field=models.IntegerField(default=555, verbose_name='phone number'),
        ),
        migrations.AlterField(
            model_name='card',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_list', to='cards.category', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='card',
            name='fund',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='funds', to='cards.fund', verbose_name='fund'),
        ),
        migrations.AlterField(
            model_name='cardimage',
            name='card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card_images', to='cards.card', verbose_name='card'),
        ),
        migrations.AlterField(
            model_name='donations',
            name='card',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='donations', to='cards.card', verbose_name='card'),
        ),
        migrations.AlterField(
            model_name='donations',
            name='payment_dt',
            field=models.DateTimeField(blank=True, db_column='payment_dt', default=datetime.datetime(2022, 10, 6, 9, 58, 8, 359907), null=True, verbose_name='payment_dt'),
        ),
        migrations.AlterField(
            model_name='donations',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
