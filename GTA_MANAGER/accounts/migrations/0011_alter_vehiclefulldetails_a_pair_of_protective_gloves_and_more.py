# Generated by Django 5.1.4 on 2024-12-30 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_customuser_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='a_pair_of_protective_gloves',
            field=models.CharField(blank=True, choices=[('Да', 'Да'), ('Не', 'Не')], default='Не', max_length=2),
        ),
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='adr_validity',
            field=models.DateField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='collection_container',
            field=models.CharField(blank=True, choices=[('Да', 'Да'), ('Не', 'Не')], default='Не', max_length=2),
        ),
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='eye_protection',
            field=models.CharField(blank=True, choices=[('Да', 'Да'), ('Не', 'Не')], default='Не', max_length=2),
        ),
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='eye_wash_liquid',
            field=models.CharField(blank=True, choices=[('Да', 'Да'), ('Не', 'Не')], default='Не', max_length=2),
        ),
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='fire_extinguishers',
            field=models.CharField(blank=True, choices=[('Да', 'Да'), ('Не', 'Не')], default='Не', max_length=2),
        ),
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='fitness_protocol_validity',
            field=models.DateField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='insurance_casco_validity',
            field=models.DateField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='insurance_civil_liability',
            field=models.DateField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='manhole_cover',
            field=models.CharField(blank=True, choices=[('Да', 'Да'), ('Не', 'Не')], default='Не', max_length=2),
        ),
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='mask',
            field=models.CharField(blank=True, choices=[('Да', 'Да'), ('Не', 'Не')], default='Не', max_length=2),
        ),
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='portable_lighting_fixture',
            field=models.CharField(blank=True, choices=[('Да', 'Да'), ('Не', 'Не')], default='Не', max_length=2),
        ),
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='reflective_vest',
            field=models.CharField(blank=True, choices=[('Да', 'Да'), ('Не', 'Не')], default='Не', max_length=2),
        ),
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='shovel',
            field=models.CharField(blank=True, choices=[('Да', 'Да'), ('Не', 'Не')], default='Не', max_length=2),
        ),
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='tachograph_validity',
            field=models.DateField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='technical_check_validity',
            field=models.DateField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='two_warning_signs',
            field=models.CharField(blank=True, choices=[('Да', 'Да'), ('Не', 'Не')], default='Не', max_length=2),
        ),
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='wheel_chock',
            field=models.CharField(blank=True, choices=[('Да', 'Да'), ('Не', 'Не')], default='Нe', max_length=2),
        ),
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='written_instructions_colored',
            field=models.CharField(blank=True, choices=[('Да', 'Да'), ('Не', 'Не')], default='Не', max_length=2),
        ),
        migrations.AlterField(
            model_name='vehicles',
            name='adr',
            field=models.CharField(choices=[('Да', 'Да'), ('Не', 'Не')], default='Да', max_length=2),
        ),
        migrations.AlterField(
            model_name='vehicles',
            name='brand',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='vehicles',
            name='model',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='vehicles',
            name='type',
            field=models.CharField(choices=[('ВЛЕКАЧ', 'ВЛЕКАЧ'), ('ЦИСТЕРНА', 'ЦИСТЕРНА'), ('АВТОМОБИЛ', 'АВТОМОБИЛ')], default='АВТОМОБИЛ', max_length=50),
        ),
    ]
