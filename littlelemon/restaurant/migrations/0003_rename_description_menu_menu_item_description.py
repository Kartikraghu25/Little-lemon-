# Generated by Django 4.1.3 on 2025-02-08 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_menu_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='description',
            new_name='menu_item_description',
        ),
    ]
