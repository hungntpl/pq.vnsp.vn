# Generated by Django 3.2.18 on 2023-04-01 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cs', '0010_auto_20230401_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cs',
            name='DGDManDate',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='cs',
            name='PCManDate',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='cs',
            name='PIManDate',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='cs',
            name='PRManDate',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='cs',
            name='QAManDate',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='cs',
            name='QCManDate',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date'),
        ),
    ]
