# Generated by Django 3.1 on 2022-03-07 12:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('service_contract', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicecontract',
            name='order_num',
            field=models.CharField(default=uuid.UUID('93786dc5-d053-4c7e-8680-f86367dbb964'), max_length=100),
        ),
    ]
