# Generated by Django 5.1.4 on 2024-12-19 17:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_vehiclefulldetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiclefulldetails',
            name='vehicle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='full_details', to='accounts.vehicles'),
        ),
    ]
