# Generated by Django 3.2.18 on 2023-05-06 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cs', '0099_auto_20230506_0705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csqc',
            name='Straightness',
        ),
        migrations.AlterField(
            model_name='csqc',
            name='Straight',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Straightness'),
        ),
    ]
