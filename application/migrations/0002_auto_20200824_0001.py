# Generated by Django 3.0.6 on 2020-08-24 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place_information',
            name='sec_place_1',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
        migrations.AddField(
            model_name='place_information',
            name='sec_place_2',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
        migrations.AddField(
            model_name='place_information',
            name='sec_place_3',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
        migrations.AddField(
            model_name='place_information',
            name='sec_place_4',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
    ]
