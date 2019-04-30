# Generated by Django 2.2 on 2019-04-30 02:13

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [("core", "0011_delete_photo")]

    operations = [
        migrations.AlterField(
            model_name="articlepage",
            name="body",
            field=wagtail.core.fields.StreamField(
                [
                    ("paragraph", wagtail.core.blocks.RichTextBlock()),
                    (
                        "photo",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                (
                                    "caption",
                                    wagtail.core.blocks.RichTextBlock(
                                        features=["bold", "italic"], required=False
                                    ),
                                ),
                                (
                                    "size",
                                    wagtail.core.blocks.ChoiceBlock(
                                        choices=[
                                            ("small", "Small"),
                                            ("medium", "Medium"),
                                            ("large", "Large"),
                                        ],
                                        help_text="Width of image in article.",
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "photo_gallery",
                        wagtail.core.blocks.ListBlock(
                            wagtail.core.blocks.StructBlock(
                                [
                                    (
                                        "image",
                                        wagtail.images.blocks.ImageChooserBlock(),
                                    ),
                                    (
                                        "caption",
                                        wagtail.core.blocks.RichTextBlock(
                                            features=["bold", "italic"], required=False
                                        ),
                                    ),
                                ]
                            ),
                            icon="image",
                        ),
                    ),
                    (
                        "embed",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "embed",
                                    wagtail.embeds.blocks.EmbedBlock(
                                        help_text="URL to the content to embed."
                                    ),
                                )
                            ]
                        ),
                    ),
                ]
            ),
        )
    ]
