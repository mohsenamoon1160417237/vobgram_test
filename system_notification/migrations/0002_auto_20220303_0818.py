# Generated by Django 3.1 on 2022-03-03 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_notification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemnotification',
            name='data_type',
            field=models.CharField(max_length=50, null=True),
        ),
    ]