# Generated by Django 3.2.18 on 2023-05-13 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sa', '0021_sa_appdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sa',
            name='PipeEdgeNoteT',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Pipe E Tole.'),
        ),
    ]