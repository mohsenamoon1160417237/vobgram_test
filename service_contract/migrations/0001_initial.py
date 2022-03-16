# Generated by Django 3.1 on 2022-03-16 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('business_service', '0001_initial'),
        ('accounts', '0002_auto_20220316_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceContract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('canceled', models.BooleanField(default=False)),
                ('bid', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service_contract', to='business_service.servicerequestbid')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_contracts', to='accounts.customerprofile')),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_contracts', to='accounts.businessprofile')),
                ('service_request', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service_contracts', to='business_service.servicerequest')),
                ('sup_visor', models.ManyToManyField(related_name='contracts', to='accounts.SupVsProfile')),
            ],
        ),
        migrations.CreateModel(
            name='ContractFactor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('payment_service', models.CharField(max_length=100)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='factors', to='service_contract.servicecontract')),
            ],
        ),
        migrations.CreateModel(
            name='ContractCondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conditions', to='service_contract.servicecontract')),
            ],
        ),
        migrations.CreateModel(
            name='ContractAssign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_assigned', models.BooleanField(default=False)),
                ('customer_assigned', models.BooleanField(default=False)),
                ('contract', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='contract_assign', to='service_contract.servicecontract')),
            ],
        ),
    ]
