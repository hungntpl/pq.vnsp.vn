# Generated by Django 3.2.18 on 2023-05-03 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cs', '0074_alter_cs_imagespec'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cs',
            name='CVer',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='Ver'),
        ),
    ]
