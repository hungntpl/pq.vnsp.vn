# Generated by Django 3.2.18 on 2023-05-12 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sa', '0017_alter_sa_sano'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sa',
            name='DGDJudgment',
            field=models.CharField(blank=True, choices=[('OK', 'OK'), ('NG', 'NG'), ('Remark', 'Remark')], max_length=15, null=True, verbose_name='AO Judg.'),
        ),
    ]
