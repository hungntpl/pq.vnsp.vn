# Generated by Django 3.2.18 on 2023-05-08 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('set', '0011_tmp'),
    ]

    operations = [
        migrations.AddField(
            model_name='pipegrade',
            name='T',
            field=models.FloatField(blank=True, max_length=20, null=True, verbose_name='Index'),
        ),
    ]
