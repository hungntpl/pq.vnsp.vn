# Generated by Django 3.2.18 on 2023-04-19 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cs', '0063_auto_20230419_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csqc',
            name='SurfLevel',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='S.Level'),
        ),
        migrations.AlterField(
            model_name='csqc',
            name='SurfTreat',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='S.Treat'),
        ),
    ]
