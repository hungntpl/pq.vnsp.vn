# Generated by Django 3.2.18 on 2023-05-08 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('set', '0007_pipegrade_straightness'),
    ]

    operations = [
        migrations.AddField(
            model_name='pipegrade',
            name='Index',
            field=models.FloatField(blank=True, max_length=20, null=True, verbose_name='Index'),
        ),
    ]
