# Generated by Django 4.2.3 on 2023-08-12 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('add', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advert',
            old_name='updates_at',
            new_name='updated_at',
        ),
    ]
