# Generated by Django 2.1.2 on 2018-11-09 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_details', '0013_auto_20181109_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant_details',
            name='prof',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
