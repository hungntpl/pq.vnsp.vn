# Generated by Django 3.2.18 on 2023-03-24 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cs', '0004_alter_cs_sano'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cs',
            name='SANo',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='SA Number'),
        ),
    ]
