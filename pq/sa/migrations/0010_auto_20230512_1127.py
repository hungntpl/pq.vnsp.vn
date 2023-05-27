# Generated by Django 3.2.18 on 2023-05-12 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sa', '0009_auto_20230512_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sa',
            name='DGDJudgment',
            field=models.CharField(blank=True, choices=[('OK', 'OK'), ('NG', 'NG'), ('Remark', 'Remark')], max_length=15, null=True, verbose_name='GD Judg.'),
        ),
        migrations.AlterField(
            model_name='sa',
            name='InBead',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Inside Bead'),
        ),
        migrations.AlterField(
            model_name='sa',
            name='SurfLevel',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Surface Level'),
        ),
    ]
