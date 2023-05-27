# Generated by Django 3.2.18 on 2023-05-05 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cs', '0090_cs_shape'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cs',
            name='Shape',
        ),
        migrations.AlterField(
            model_name='cs',
            name='SKind',
            field=models.CharField(blank=True, choices=[('Round', 'Round'), ('Square', 'Square'), ('Oval', 'Oval'), ('Ellipse', 'Ellipse')], max_length=50, null=True, verbose_name='Shape'),
        ),
    ]