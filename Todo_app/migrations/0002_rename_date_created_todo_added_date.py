# Generated by Django 3.2.5 on 2021-07-16 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='date_created',
            new_name='added_date',
        ),
    ]
