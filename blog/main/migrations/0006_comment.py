# Generated by Django 4.0.1 on 2022-01-16 09:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0005_alter_post_options_rename_created_post_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='main.post')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_name', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
