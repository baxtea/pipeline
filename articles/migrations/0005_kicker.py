# Generated by Django 2.0.7 on 2018-07-19 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20180717_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kicker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
    ]