# Generated by Django 3.2.18 on 2023-05-06 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cs', '0102_auto_20230506_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csqc',
            name='ChMo',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Molybdenum'),
        ),
        migrations.AlterField(
            model_name='csqc',
            name='ChN',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Nitrogen'),
        ),
        migrations.AlterField(
            model_name='csqc',
            name='ChNb',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Niobium'),
        ),
        migrations.AlterField(
            model_name='csqc',
            name='ChTi',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Titanium'),
        ),
        migrations.AlterField(
            model_name='csqc',
            name='ChZr',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Zinc'),
        ),
    ]