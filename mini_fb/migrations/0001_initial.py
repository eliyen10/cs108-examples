# Generated by Django 2.2.7 on 2021-11-04 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(blank=True)),
                ('last_name', models.TextField(blank=True)),
                ('city', models.TextField(blank=True)),
                ('email_address', models.TextField(blank=True)),
                ('profile_img_url', models.TextField(blank=True)),
            ],
        ),
    ]