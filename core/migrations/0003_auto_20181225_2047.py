# Generated by Django 2.1.4 on 2018-12-25 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("core", "0002_auto_20181225_2045")]

    operations = [
        migrations.AlterField(
            model_name="articleauthor",
            name="staff_page",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="core.StaffPage",
            ),
        )
    ]
