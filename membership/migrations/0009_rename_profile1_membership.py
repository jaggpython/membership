# Generated by Django 4.1.2 on 2022-10-20 07:13

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('membership', '0008_profile1_delete_profile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile1',
            new_name='Membership',
        ),
    ]
