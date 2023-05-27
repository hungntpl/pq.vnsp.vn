# Generated by Django 3.2.18 on 2023-05-11 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('set', '0014_remove_pipegrade_t'),
    ]

    operations = [
        migrations.CreateModel(
            name='surflevel',
            fields=[
                ('SurfLevel', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Surface level')),
                ('ENotes', models.CharField(blank=True, max_length=500, null=True, verbose_name='English Note')),
                ('VNotes', models.CharField(blank=True, max_length=500, null=True, verbose_name='Vietnamese Note')),
                ('LastUser', models.CharField(blank=True, max_length=50, null=True, verbose_name='LastUser')),
                ('LastimeUser', models.DateTimeField(blank=True, null=True, verbose_name='LastimeUser')),
            ],
        ),
    ]
