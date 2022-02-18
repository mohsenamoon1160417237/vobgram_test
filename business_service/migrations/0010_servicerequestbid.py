# Generated by Django 3.1 on 2022-02-17 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_admindataconfirm_comment'),
        ('business_service', '0009_auto_20220217_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceRequestBid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suggestion_text', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('days', models.IntegerField()),
                ('bidder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_request_bids', to='accounts.businessprofile')),
                ('service_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_request_bids', to='business_service.servicerequest')),
            ],
        ),
    ]
