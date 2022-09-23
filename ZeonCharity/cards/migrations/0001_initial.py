# Generated by Django 4.0.5 on 2022-09-22 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_column='title', max_length=100)),
                ('description', models.TextField(db_column='description', max_length=1000)),
                ('target_amnt', models.FloatField(db_column='target_amnt', default=0)),
                ('total_amnt', models.FloatField(db_column='total_amnt', default=0)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('deadline', models.DateTimeField(blank=True, db_column='deadline', null=True)),
                ('is_urgent', models.BooleanField(default=False)),
                ('is_approved', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Card',
                'verbose_name_plural': 'Cards',
                'db_table': 'card',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_column='title', max_length=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_column='title', max_length=100)),
                ('description', models.TextField(db_column='description', max_length=1000)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
            options={
                'verbose_name': 'Fund',
                'verbose_name_plural': 'Funds',
                'db_table': 'fund',
            },
        ),
        migrations.CreateModel(
            name='Donations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(db_column='user_id')),
                ('donation_amnt', models.FloatField(db_column='donation_amnt', default=0)),
                ('payment_dt', models.DateTimeField(blank=True, db_column='payment_dt', null=True)),
                ('card', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='donations', to='cards.card')),
            ],
            options={
                'verbose_name': 'Donation',
                'verbose_name_plural': 'Donations',
                'db_table': 'donation',
            },
        ),
        migrations.CreateModel(
            name='CardImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card_images', to='cards.card')),
            ],
            options={
                'verbose_name': 'Card Image',
                'verbose_name_plural': 'Card Images',
                'db_table': 'card_images',
            },
        ),
        migrations.AddField(
            model_name='card',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_list', to='cards.category'),
        ),
        migrations.AddField(
            model_name='card',
            name='fund',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='funds', to='cards.fund'),
        ),
    ]