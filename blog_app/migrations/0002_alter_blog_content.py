# Generated by Django 5.1.4 on 2024-12-29 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(max_length=2000),
        ),
    ]