# Generated by Django 5.1.4 on 2024-12-23 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_vehicles_adr_alter_vehicles_condition_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='a_pair_of_protective_gloves',
            field=models.CharField(blank=True, choices=[('Да', 'Да'), ('Не', 'Не')], default='Не'),
        ),
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='collection_container',
            field=models.CharField(blank=True, choices=[('Да', 'Да'), ('Не', 'Не')], default='Не'),
        ),
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='eye_protection',
            field=models.CharField(blank=True, choices=[('Да', 'Да'), ('Не', 'Не')], default='Не'),
        ),
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='eye_wash_liquid',
            field=models.CharField(blank=True, choices=[('Да', 'Да'), ('Не', 'Не')], default='Не'),
        ),
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='fire_extinguishers',
            field=models.CharField(blank=True, choices=[('Да', 'Да'), ('Не', 'Не')], default='Не'),
        ),
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='manhole_cover',
            field=models.CharField(blank=True, choices=[('Да', 'Да'), ('Не', 'Не')], default='Не'),
        ),
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='mask',
            field=models.CharField(blank=True, choices=[('Да', 'Да'), ('Не', 'Не')], default='Не'),
        ),
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='portable_lighting_fixture',
            field=models.CharField(blank=True, choices=[('Да', 'Да'), ('Не', 'Не')], default='Не'),
        ),
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='reflective_vest',
            field=models.CharField(blank=True, choices=[('Да', 'Да'), ('Не', 'Не')], default='Не'),
        ),
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='shovel',
            field=models.CharField(blank=True, choices=[('Да', 'Да'), ('Не', 'Не')], default='Не'),
        ),
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='two_warning_signs',
            field=models.CharField(blank=True, choices=[('Да', 'Да'), ('Не', 'Не')], default='Не'),
        ),
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='wheel_chock',
            field=models.CharField(blank=True, choices=[('Да', 'Да'), ('Не', 'Не')], default='Нe'),
        ),
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='written_instructions_colored',
            field=models.CharField(blank=True, choices=[('Да', 'Да'), ('Не', 'Не')], default='Не'),
        ),
    ]
