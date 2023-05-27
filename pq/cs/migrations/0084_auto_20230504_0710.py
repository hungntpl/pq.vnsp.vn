# Generated by Django 3.2.18 on 2023-05-04 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cs', '0083_alter_cs_imagespec'),
    ]

    operations = [
        migrations.AddField(
            model_name='cs',
            name='Demand',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Demand'),
        ),
        migrations.AddField(
            model_name='cs',
            name='Enduser',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='End User'),
        ),
        migrations.AddField(
            model_name='cs',
            name='Event',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Event'),
        ),
    ]
