# Generated by Django 3.1 on 2022-03-08 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_contract', '0005_auto_20220308_0828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicecontract',
            name='order_num',
        ),
    ]
