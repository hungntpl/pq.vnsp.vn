# Generated by Django 3.2.18 on 2023-05-12 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sa', '0011_auto_20230512_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sa',
            name='PipeStd',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Standard'),
        ),
    ]