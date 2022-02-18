# Generated by Django 3.1 on 2022-02-17 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_service', '0007_auto_20220217_2119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicerequest',
            name='acceptors',
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='max_days',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
