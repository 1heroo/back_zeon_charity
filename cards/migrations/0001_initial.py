# Generated by Django 4.1.1 on 2022-10-10 21:59

from django.db import migrations, models
import django.db.models.deletion
import location_field.models.plain


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_column='title', max_length=100, verbose_name='title')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='image')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='FundraisingCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_column='title', max_length=100, verbose_name='title')),
                ('description', models.TextField(db_column='description', max_length=1000, verbose_name='description')),
                ('target_amnt', models.FloatField(db_column='target_amnt', default=0, verbose_name='target_amnt')),
                ('deadline', models.DateTimeField(blank=True, db_column='deadline', null=True, verbose_name='deadline')),
                ('contacts', models.TextField(blank=True, db_column='contacts', max_length=500, null=True, verbose_name='contacts')),
                ('is_approved', models.BooleanField(default=False)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_list', to='cards.category', verbose_name='category')),
            ],
            options={
                'verbose_name': 'Fundraising Card',
                'verbose_name_plural': 'Fundraising Cards',
                'db_table': 'fundraising_card',
            },
        ),
        migrations.CreateModel(
            name='VolunteeringCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_column='title', max_length=100, verbose_name='title')),
                ('description', models.TextField(db_column='description', max_length=1000, verbose_name='description')),
                ('start_dt', models.DateTimeField(blank=True, db_column='start_dt', null=True, verbose_name='start_dt')),
                ('end_dt', models.DateTimeField(blank=True, db_column='end_dt', null=True, verbose_name='end_dt')),
                ('responsibility', models.TextField(db_column='responsibility', max_length=1000, verbose_name='responsibility')),
                ('requirements', models.TextField(db_column='requirements', max_length=1000, verbose_name='requirements')),
                ('contacts', models.TextField(db_column='contacts', max_length=500, verbose_name='contacts')),
            ],
            options={
                'verbose_name': 'Volunteering Card',
                'verbose_name_plural': 'Volunteering Cards',
                'db_table': 'volunteering_card',
            },
        ),
        migrations.CreateModel(
            name='VolunteeringCardLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', location_field.models.plain.PlainLocationField(max_length=63, verbose_name='location')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card_images', to='cards.volunteeringcard', verbose_name='card')),
            ],
            options={
                'verbose_name': 'Volunteering Card Location',
                'verbose_name_plural': 'Volunteering Card Locations',
                'db_table': 'card_locations',
            },
        ),
        migrations.CreateModel(
            name='VolunteeringCardImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/volunteering/', verbose_name='image')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vol_card_images', to='cards.volunteeringcard', verbose_name='card')),
            ],
            options={
                'verbose_name': 'Volunteering Card Image',
                'verbose_name_plural': 'Volunteering Card Images',
                'db_table': 'vol_card_images',
            },
        ),
        migrations.CreateModel(
            name='VolunteeringCardDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='documents/')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card_documents', to='cards.volunteeringcard', verbose_name='card')),
            ],
            options={
                'verbose_name': 'Volunteering Card Document',
                'verbose_name_plural': 'Volunteering Card Documents',
                'db_table': 'card_docs',
            },
        ),
        migrations.CreateModel(
            name='FundraisingCardImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/fundraising', verbose_name='image')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fund_card_images', to='cards.fundraisingcard', verbose_name='card')),
            ],
            options={
                'verbose_name': 'Fundraising Card Image',
                'verbose_name_plural': 'Fundraising Card Images',
                'db_table': 'fun_card_images',
            },
        ),
    ]
