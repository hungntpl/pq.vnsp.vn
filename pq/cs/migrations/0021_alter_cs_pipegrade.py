# Generated by Django 3.2.18 on 2023-04-02 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cs', '0020_pipegrade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cs',
            name='PipeGrade',
            field=models.ForeignKey(blank=True, max_length=50, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cs.pipegrade', verbose_name='Pipe Grade'),
        ),
    ]
