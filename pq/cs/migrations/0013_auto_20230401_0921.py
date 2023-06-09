# Generated by Django 3.2.18 on 2023-04-01 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cs', '0012_alter_cs_asmandate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cs',
            name='ASManJudgment',
            field=models.CharField(blank=True, choices=[('OK', 'OK'), ('NG', 'NG'), ('Remark', 'Remark')], max_length=15, null=True, verbose_name='AS J.'),
        ),
        migrations.AlterField(
            model_name='cs',
            name='DGDJudgment',
            field=models.CharField(blank=True, choices=[('OK', 'OK'), ('NG', 'NG'), ('Remark', 'Remark')], max_length=15, null=True, verbose_name='DGD J.'),
        ),
        migrations.AlterField(
            model_name='cs',
            name='PCManJudgment',
            field=models.CharField(blank=True, choices=[('OK', 'OK'), ('NG', 'NG'), ('Remark', 'Remark')], max_length=15, null=True, verbose_name='PC J.'),
        ),
        migrations.AlterField(
            model_name='cs',
            name='PIManJudgment',
            field=models.CharField(blank=True, choices=[('OK', 'OK'), ('NG', 'NG'), ('Remark', 'Remark')], max_length=15, null=True, verbose_name='PI J.'),
        ),
        migrations.AlterField(
            model_name='cs',
            name='PRManJudgment',
            field=models.CharField(blank=True, choices=[('OK', 'OK'), ('NG', 'NG'), ('Remark', 'Remark')], max_length=15, null=True, verbose_name='PR J.'),
        ),
        migrations.AlterField(
            model_name='cs',
            name='QAManJudgment',
            field=models.CharField(blank=True, choices=[('OK', 'OK'), ('NG', 'NG'), ('Remark', 'Remark')], max_length=15, null=True, verbose_name='QA J.'),
        ),
        migrations.AlterField(
            model_name='cs',
            name='QCManJudgment',
            field=models.CharField(blank=True, choices=[('OK', 'OK'), ('NG', 'NG'), ('Remark', 'Remark')], max_length=15, null=True, verbose_name='QC J.'),
        ),
    ]
