# Generated by Django 3.2.18 on 2023-04-08 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cs', '0039_coilprocess'),
    ]

    operations = [
        migrations.AddField(
            model_name='coilprocess',
            name='No',
            field=models.SmallIntegerField(default=1, verbose_name='No'),
        ),
    ]
