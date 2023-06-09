# Generated by Django 3.2.18 on 2023-05-06 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cs', '0101_auto_20230506_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csqc',
            name='ChAL',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Aluminium'),
        ),
        migrations.AlterField(
            model_name='csqc',
            name='ChC',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Carbon'),
        ),
        migrations.AlterField(
            model_name='csqc',
            name='ChCr',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Chromium'),
        ),
        migrations.AlterField(
            model_name='csqc',
            name='ChMn',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Manganese'),
        ),
        migrations.AlterField(
            model_name='csqc',
            name='ChNi',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Nickel'),
        ),
        migrations.AlterField(
            model_name='csqc',
            name='ChP',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Phosphorus'),
        ),
        migrations.AlterField(
            model_name='csqc',
            name='ChS',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Sulphur'),
        ),
        migrations.AlterField(
            model_name='csqc',
            name='ChSi',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Silicon'),
        ),
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
