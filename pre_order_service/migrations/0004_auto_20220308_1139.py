# Generated by Django 3.1 on 2022-03-08 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pre_order_service', '0003_auto_20220308_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preorderservice',
            name='off_price',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
    ]