# Generated by Django 3.2.18 on 2023-05-13 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('set', '0016_emailreport'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailreport',
            name='Remarks',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Remarks'),
        ),
    ]
