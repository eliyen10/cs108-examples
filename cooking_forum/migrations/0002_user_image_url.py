# Generated by Django 2.2.7 on 2021-11-22 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooking_forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image_url',
            field=models.URLField(blank=True),
        ),
    ]
