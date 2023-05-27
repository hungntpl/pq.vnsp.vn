# Generated by Django 3.2.18 on 2023-05-06 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cs', '0097_alter_cs_pipegrade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csqc',
            name='TS',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='TS(N/mm2)'),
        ),
        migrations.AlterField(
            model_name='csqc',
            name='YP',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='YP(%)'),
        ),
    ]
