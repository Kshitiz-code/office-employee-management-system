# Generated by Django 4.0.2 on 2022-02-08 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person',
            new_name='Employee',
        ),
    ]
