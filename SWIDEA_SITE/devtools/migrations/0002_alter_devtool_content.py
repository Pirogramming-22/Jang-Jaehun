# Generated by Django 5.1.4 on 2025-01-15 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devtools', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devtool',
            name='content',
            field=models.TextField(max_length=400, verbose_name='내용'),
        ),
    ]
