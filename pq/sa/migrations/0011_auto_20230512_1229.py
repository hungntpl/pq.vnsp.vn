# Generated by Django 3.2.18 on 2023-05-12 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sa', '0010_auto_20230512_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sa',
            name='PKind',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Kind'),
        ),
        migrations.AlterField(
            model_name='sa',
            name='SKind',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Shape'),
        ),
    ]
