# Generated by Django 3.2.18 on 2023-04-22 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cs', '0069_alter_csqc_hardness'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cspi',
            name='RTH2',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='RTH2'),
        ),
    ]
