# Generated by Django 3.1.2 on 2020-10-12 21:43

import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_homepage_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homepage",
            name="body",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "title",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "text",
                                    wagtail.core.blocks.CharBlock(
                                        help_text="Text to display", required=True
                                    ),
                                )
                            ]
                        ),
                    ),
                    (
                        "cards",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "cards",
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.StructBlock(
                                            [
                                                (
                                                    "title",
                                                    wagtail.core.blocks.CharBlock(
                                                        help_text="Bold title text for this card.",
                                                        max_length=100,
                                                    ),
                                                ),
                                                (
                                                    "text",
                                                    wagtail.core.blocks.TextBlock(
                                                        help_text="Optional text for this card.",
                                                        max_length=255,
                                                        required=False,
                                                    ),
                                                ),
                                                (
                                                    "image",
                                                    wagtail.images.blocks.ImageChooserBlock(
                                                        help_text="Image will be auto. cropped to 570x770"
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                )
                            ]
                        ),
                    ),
                ],
                blank=True,
                null=True,
            ),
        ),
    ]
