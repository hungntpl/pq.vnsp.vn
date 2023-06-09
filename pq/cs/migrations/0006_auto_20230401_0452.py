# Generated by Django 3.2.18 on 2023-04-01 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cs', '0005_alter_cs_sano'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cs',
            name='ASManJudgment',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='AS Judgm'),
        ),
        migrations.AlterField(
            model_name='cs',
            name='ASManNote',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='AS Note'),
        ),
        migrations.AlterField(
            model_name='cs',
            name='DGDJudgment',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='DGD Judgm'),
        ),
        migrations.AlterField(
            model_name='cs',
            name='DGDNote',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='DGD Note'),
        ),
        migrations.AlterField(
            model_name='cs',
            name='PCManJudgment',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='PCM Judgm'),
        ),
        migrations.AlterField(
            model_name='cs',
            name='PCManNote',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='PC Note'),
        ),
        migrations.AlterField(
            model_name='cs',
            name='PIManJudgment',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='PI Judgm'),
        ),
        migrations.AlterField(
            model_name='cs',
            name='PIManNote',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='PI Note'),
        ),
        migrations.AlterField(
            model_name='cs',
            name='PRManJudgment',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='PRM Judgm'),
        ),
        migrations.AlterField(
            model_name='cs',
            name='PRManNote',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='PR Note'),
        ),
        migrations.AlterField(
            model_name='cs',
            name='QAManJudgment',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='QA Judgm'),
        ),
        migrations.AlterField(
            model_name='cs',
            name='QAManNote',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='QA Note'),
        ),
        migrations.AlterField(
            model_name='cs',
            name='QCManJudgment',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='QC Judgm'),
        ),
        migrations.AlterField(
            model_name='cs',
            name='QCManNote',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='QC Note'),
        ),
    ]
