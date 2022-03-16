# Generated by Django 3.1 on 2022-03-16 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreOrderService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('registered_count', models.IntegerField(default=0)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('off_amount', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('off_price', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pre_order_services', to='accounts.businessprofile')),
                ('user_register', models.ManyToManyField(related_name='pre_order_services', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('note', models.CharField(max_length=300)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_attrs', to='pre_order_service.preorderservice')),
            ],
        ),
    ]
