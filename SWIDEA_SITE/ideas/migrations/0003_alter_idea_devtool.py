# Generated by Django 5.1.4 on 2025-01-15 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0002_alter_idea_devtool'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='devtool',
            field=models.CharField(max_length=24, verbose_name='개발툴'),
        ),
    ]
