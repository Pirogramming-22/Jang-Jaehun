# Generated by Django 5.1.5 on 2025-01-19 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='like',
            new_name='likes',
        ),
    ]