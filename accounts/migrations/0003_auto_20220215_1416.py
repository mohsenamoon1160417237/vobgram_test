# Generated by Django 3.1 on 2022-02-15 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220215_1405'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adminprofile',
            old_name='checked_data_number',
            new_name='confirmed_data_number',
        ),
    ]