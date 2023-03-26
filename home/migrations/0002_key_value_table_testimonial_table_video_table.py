# Generated by Django 4.1.7 on 2023-03-26 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="key_value_table",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("key", models.CharField(max_length=100)),
                ("value", models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name="testimonial_table",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("heading", models.CharField(max_length=100)),
                ("text", models.TextField(max_length=1000)),
                ("name", models.CharField(max_length=50)),
                ("location", models.CharField(max_length=100)),
                ("show", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="video_table",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("heading", models.CharField(max_length=50)),
                ("image_link", models.URLField(max_length=300)),
                ("ytplaylist_link", models.URLField(max_length=300)),
            ],
        ),
    ]
