# Generated by Django 3.0.6 on 2020-08-29 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0008_predictions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictions',
            name='reference_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.countering'),
        ),
    ]