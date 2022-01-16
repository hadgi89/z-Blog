# Generated by Django 4.0.1 on 2022-01-14 12:20

import django.core.validators
from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_post_category_alter_post_desc_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='sourse',
            new_name='post_sourse',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to=main.models.post_img_dir, validators=[django.core.validators.FileExtensionValidator(['jpeg', 'jpg', 'png', 'webp'])], verbose_name='Изображение'),
        ),
    ]
