# Generated by Django 3.2.18 on 2023-04-03 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cs', '0025_alter_cs_newinq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cs',
            name='PreBy',
            field=models.CharField(blank=True, default='Lâm', max_length=50, null=True, verbose_name='Pre by'),
        ),
    ]
