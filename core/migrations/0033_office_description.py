# Generated by Django 2.2.9 on 2020-02-15 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("core", "0032_auto_20200215_1845")]

    operations = [
        migrations.AddField(
            model_name="office",
            name="description",
            field=models.CharField(default="", max_length=255),
            preserve_default=False,
        )
    ]