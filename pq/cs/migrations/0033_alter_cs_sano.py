# Generated by Django 3.2.18 on 2023-04-08 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sa', '0004_auto_20230401_1053'),
        ('cs', '0032_alter_cs_pipegrade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cs',
            name='SANo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sa.sa', verbose_name='SA Number'),
        ),
    ]
