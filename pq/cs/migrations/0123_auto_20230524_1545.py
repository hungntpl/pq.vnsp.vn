# Generated by Django 3.2.18 on 2023-05-24 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cs', '0122_alter_coilprocess_cgrade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coilprocess',
            name='CWTOrder',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Coil WT'),
        ),
        migrations.AlterField(
            model_name='coilprocess',
            name='SCoilWidth',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Coil Width'),
        ),
    ]