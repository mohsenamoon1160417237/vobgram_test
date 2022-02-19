# Generated by Django 3.1 on 2022-02-19 07:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business_service', '0012_servicecontract'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_rating', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('service_note', models.CharField(max_length=300)),
                ('service_contract', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='service_review', to='business_service.servicecontract')),
                ('service_request', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='service_review', to='business_service.servicerequest')),
            ],
        ),
    ]
