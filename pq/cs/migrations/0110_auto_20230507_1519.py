# Generated by Django 3.2.18 on 2023-05-07 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cs', '0109_alter_cs_cvernote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cs',
            name='ASManJudgment',
            field=models.CharField(blank=True, choices=[('OK', 'OK'), ('NG', 'NG'), ('Remark', 'Remark')], max_length=15, null=True, verbose_name='AS Judgement'),
        ),
        migrations.AlterField(
            model_name='cs',
            name='DGDJudgment',
            field=models.CharField(blank=True, choices=[('OK', 'OK'), ('NG', 'NG'), ('Remark', 'Remark')], max_length=15, null=True, verbose_name='DGD Judgement'),
        ),
        migrations.AlterField(
            model_name='cs',
            name='PCManJudgment',
            field=models.CharField(blank=True, choices=[('OK', 'OK'), ('NG', 'NG'), ('Remark', 'Remark')], max_length=15, null=True, verbose_name='PC Judgement'),
        ),
        migrations.AlterField(
            model_name='cs',
            name='PIManJudgment',
            field=models.CharField(blank=True, choices=[('OK', 'OK'), ('NG', 'NG'), ('Remark', 'Remark')], max_length=15, null=True, verbose_name='PI Judgement'),
        ),
        migrations.AlterField(
            model_name='cs',
            name='PRManJudgment',
            field=models.CharField(blank=True, choices=[('OK', 'OK'), ('NG', 'NG'), ('Remark', 'Remark')], max_length=15, null=True, verbose_name='PR Judgement'),
        ),
        migrations.AlterField(
            model_name='cs',
            name='QAManJudgment',
            field=models.CharField(blank=True, choices=[('OK', 'OK'), ('NG', 'NG'), ('Remark', 'Remark')], max_length=15, null=True, verbose_name='QA Judgement'),
        ),
        migrations.AlterField(
            model_name='cs',
            name='QCManJudgment',
            field=models.CharField(blank=True, choices=[('OK', 'OK'), ('NG', 'NG'), ('Remark', 'Remark')], max_length=15, null=True, verbose_name='QC Judgement'),
        ),
    ]
