# Generated by Django 4.0.1 on 2022-01-16 09:05

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_post_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created_at',), 'verbose_name': 'Публикация', 'verbose_name_plural': 'Публикации'},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='tag',
            new_name='tags',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='updated',
            new_name='updated_at',
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Содержание'),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
