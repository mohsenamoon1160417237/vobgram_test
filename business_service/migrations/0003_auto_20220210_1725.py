# Generated by Django 3.1 on 2022-02-10 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220210_1642'),
        ('business_service', '0002_auto_20220210_1642'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='businessskill',
            unique_together={('valid_skill', 'business_profile')},
        ),
    ]