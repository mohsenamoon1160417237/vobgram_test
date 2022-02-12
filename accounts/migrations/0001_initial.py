# Generated by Django 3.1 on 2022-02-10 10:06

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('phone_number', models.CharField(max_length=12, unique=True)),
                ('user_type', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('registered', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonalProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=30, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(4)])),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='personal_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100, unique=True)),
                ('company_phone_number', models.CharField(max_length=14)),
                ('service_number', models.PositiveIntegerField(default=0)),
                ('service_rate', models.PositiveIntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='business_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AdminProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmed_data_number', models.PositiveIntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admin_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AdminDataConfirm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_type', models.CharField(max_length=30)),
                ('data_value', models.CharField(max_length=30)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('comment', models.TextField(blank=True, null=True)),
                ('date_time', models.DateTimeField(null=True)),
                ('is_latest', models.BooleanField(default=True)),
                ('admin_profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_data_confirms', to='accounts.adminprofile')),
                ('business_profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_confirm', to='accounts.businessprofile')),
            ],
        ),
    ]
