# Generated by Django 5.1.4 on 2024-12-30 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_vehiclefulldetails_adr_validity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='reflective_vest',
            field=models.CharField(choices=[('Да', 'Да'), ('Не', 'Не')], default='Не', max_length=2),
        ),
        migrations.AlterField(
            model_name='vehiclefulldetails',
            name='wheel_chock',
            field=models.CharField(blank=True, choices=[('Да', 'Да'), ('Не', 'Не')], default='Не', max_length=2),
        ),
    ]
