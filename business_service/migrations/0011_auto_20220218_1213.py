# Generated by Django 3.1 on 2022-02-18 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_admindataconfirm_comment'),
        ('business_service', '0010_servicerequestbid'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='servicerequestbid',
            unique_together={('bidder', 'service_request')},
        ),
    ]