# Generated by Django 4.0.4 on 2022-07-11 08:01

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0005_alter_profile_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='ProfileUser',
        ),
    ]