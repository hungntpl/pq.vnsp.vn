# Generated by Django 3.2.18 on 2023-05-04 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cs', '0080_auto_20230503_0638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csqc',
            name='Flattening',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Flat 0'),
        ),
        migrations.AlterField(
            model_name='csqc',
            name='Flattening90',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Flat 90'),
        ),
    ]