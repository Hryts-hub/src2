# Generated by Django 3.1.4 on 2020-12-08 15:46

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('manager', '0002_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
    ]
