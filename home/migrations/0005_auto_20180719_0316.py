# Generated by Django 2.0.7 on 2018-07-19 03:16

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_homepage_featured_articles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='featured_articles',
            field=wagtail.core.fields.StreamField([('article', wagtail.core.blocks.PageChooserBlock(target_model=['articles.ArticlePage'], template='home/featured_article_block.html'))], null=True),
        ),
    ]
