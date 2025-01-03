# Generated by Django 5.1.4 on 2024-12-30 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_vehiclefulldetails_a_pair_of_protective_gloves_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='adr_validity',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='fitness_protocol_validity',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='insurance_casco_validity',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='insurance_civil_liability',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='tachograph_validity',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='technical_check_validity',
            field=models.DateField(blank=True, null=True),
        ),
    ]
