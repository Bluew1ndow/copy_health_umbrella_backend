# Generated by Django 4.1.7 on 2023-09-19 20:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("members", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="key_value_table",
            options={"ordering": ["-created_at"]},
        ),
    ]