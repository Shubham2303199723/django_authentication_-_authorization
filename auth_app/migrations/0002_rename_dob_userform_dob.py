# Generated by Django 4.2.2 on 2024-04-16 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userform',
            old_name='DOB',
            new_name='dob',
        ),
    ]
