# Generated by Django 3.2.18 on 2023-05-03 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cs', '0079_alter_cs_idate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cs',
            name='Flattening',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Flattening 0'),
        ),
        migrations.AlterField(
            model_name='cs',
            name='Flattening90',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Flattening 90'),
        ),
    ]