# Generated by Django 3.1.4 on 2020-12-29 16:17

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('manager', '0022_auto_20201229_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_img',
            field=models.ImageField(default=0, upload_to='images/'),
        ),
    ]
