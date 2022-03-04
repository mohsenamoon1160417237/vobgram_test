# Generated by Django 3.1 on 2022-03-04 17:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business_service', '0003_auto_20220304_1722'),
        ('accounts', '0005_auto_20220304_1722'),
        ('service_contract', '0002_auto_20220304_1722'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ExpertProfile',
        ),
        migrations.AddField(
            model_name='supvsprofile',
            name='skill',
            field=models.ManyToManyField(related_name='sup_vs_profiles', to='business_service.ValidSkill'),
        ),
        migrations.AddField(
            model_name='supvsprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sup_vs_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='operatorprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='operator_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
