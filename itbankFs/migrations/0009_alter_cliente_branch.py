# Generated by Django 3.2.6 on 2022-08-30 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itbankFs', '0008_alter_sucursal_branch_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='branch',
            field=models.TextField(),
        ),
    ]
