# Generated by Django 2.2.1 on 2019-05-11 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("core", "0002_archivespage")]

    operations = [
        migrations.AlterField(
            model_name="term",
            name="date_started",
            field=models.DateField(blank=True, null=True),
        )
    ]
