# Generated by Django 3.1.4 on 2020-12-21 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0019_auto_20201221_1405'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SlugBook',
            new_name='Book',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='slug',
        ),
        migrations.AddField(
            model_name='comment',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='manager.book'),
        ),
        migrations.AddField(
            model_name='likebookuser',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='liked_books', to='manager.book'),
        ),
        migrations.AlterUniqueTogether(
            name='likebookuser',
            unique_together={('user', 'book')},
        ),
        migrations.RemoveField(
            model_name='likebookuser',
            name='slug',
        ),
    ]
