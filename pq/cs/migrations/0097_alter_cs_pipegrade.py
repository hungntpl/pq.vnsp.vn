# Generated by Django 3.2.18 on 2023-05-06 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('set', '0005_delete_test'),
        ('cs', '0096_auto_20230506_0539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cs',
            name='PipeGrade',
            field=models.ForeignKey(blank=True, max_length=50, null=True, on_delete=django.db.models.deletion.CASCADE, to='set.pipegrade', verbose_name='Pipe Grade'),
        ),
    ]