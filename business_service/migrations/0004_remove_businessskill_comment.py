# Generated by Django 3.1 on 2022-02-11 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business_service', '0003_auto_20220210_1725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businessskill',
            name='comment',
        ),
    ]