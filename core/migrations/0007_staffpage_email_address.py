# Generated by Django 2.0.8 on 2018-08-18 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20180818_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffpage',
            name='email_address',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
