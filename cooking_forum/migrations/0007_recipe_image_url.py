# Generated by Django 2.2.7 on 2021-12-06 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooking_forum', '0006_auto_20211206_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image_url',
            field=models.URLField(blank=True),
        ),
    ]
