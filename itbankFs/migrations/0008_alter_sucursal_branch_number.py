# Generated by Django 3.2.6 on 2022-08-30 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itbankFs', '0007_rename_direccion_sucursal_directions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sucursal',
            name='branch_number',
            field=models.TextField(),
        ),
    ]
