# Generated by Django 2.1.2 on 2018-11-26 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0021_review_review_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('review', models.TextField()),
                ('review_ordid', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
