# Generated by Django 3.2.18 on 2023-04-08 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('set', '0004_test'),
        ('cs', '0036_alter_cs_sano'),
    ]

    operations = [
        migrations.AddField(
            model_name='cs',
            name='testname',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='set.test', verbose_name='Test Name'),
        ),
    ]
