# Generated by Django 3.2.18 on 2023-04-18 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cs', '0059_auto_20230418_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cspi',
            name='PIManNote',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Note'),
        ),
        migrations.AlterField(
            model_name='cspi',
            name='PIManjudgment',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='PI jud'),
        ),
    ]
