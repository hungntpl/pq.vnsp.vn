# Generated by Django 3.2.18 on 2023-05-09 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cs', '0116_remove_cs_csap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cs',
            name='Density',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Kg/pc'),
        ),
    ]
