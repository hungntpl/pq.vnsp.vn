# Generated by Django 3.2.18 on 2023-05-07 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cs', '0105_auto_20230507_0357'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='custprocess',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='custprocess',
            name='No',
        ),
    ]
