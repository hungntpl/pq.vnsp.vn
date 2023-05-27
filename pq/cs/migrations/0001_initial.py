# Generated by Django 3.2.18 on 2023-03-23 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cs',
            fields=[
                ('CSNo', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='CS Number')),
                ('SANo', models.CharField(blank=True, max_length=100, null=True, verbose_name='SA Number')),
                ('IDate', models.DateTimeField(verbose_name='Initial date')),
                ('DLine', models.DateTimeField(verbose_name='Deadline')),
                ('CVer', models.CharField(blank=True, max_length=2, null=True, verbose_name='SA Number')),
                ('CVerDate', models.DateTimeField(blank=True, null=True, verbose_name='Issue date')),
                ('CVerNote', models.CharField(blank=True, max_length=50, null=True, verbose_name='Version note')),
                ('PVer', models.CharField(blank=True, max_length=2, null=True, verbose_name='Pervious version')),
                ('PVerDate', models.DateTimeField(blank=True, null=True, verbose_name='PreVersion date')),
                ('PVerNote', models.CharField(blank=True, max_length=50, null=True, verbose_name='PreVersion Note')),
                ('NewInq', models.CharField(blank=True, max_length=15, null=True, verbose_name='New Inquiry')),
                ('ModiC1', models.BooleanField(blank=True, null=True, verbose_name='Modi C1')),
                ('ModiC2', models.BooleanField(blank=True, null=True, verbose_name='Modi C2')),
                ('PreBy', models.CharField(blank=True, max_length=50, null=True, verbose_name='Pre by')),
                ('RecBy', models.CharField(blank=True, max_length=50, null=True, verbose_name='Rec by')),
                ('CustID', models.CharField(blank=True, max_length=15, null=True, verbose_name='Customer ID')),
                ('PartNo', models.CharField(blank=True, max_length=50, null=True, verbose_name='Part No')),
                ('PartName', models.CharField(blank=True, max_length=50, null=True, verbose_name='Part Name')),
                ('PartMaker', models.CharField(blank=True, max_length=50, null=True, verbose_name='Part Maker')),
                ('Model', models.CharField(blank=True, max_length=50, null=True, verbose_name='Model')),
                ('EstQty', models.CharField(blank=True, max_length=50, null=True, verbose_name='Estimate Qty')),
                ('EstTime', models.CharField(blank=True, max_length=50, null=True, verbose_name='Estimate Time')),
                ('EstFDeli', models.CharField(blank=True, max_length=50, null=True, verbose_name='Estimate Delivery')),
                ('EstFQty', models.CharField(blank=True, max_length=50, null=True, verbose_name='Estimate F.Qty')),
                ('SKind', models.CharField(blank=True, max_length=50, null=True, verbose_name='SKind')),
                ('PKind', models.CharField(blank=True, max_length=50, null=True, verbose_name='PKind')),
                ('OD', models.CharField(blank=True, max_length=5, null=True, verbose_name='OD')),
                ('ID', models.CharField(blank=True, max_length=5, null=True, verbose_name='ID')),
                ('WT', models.CharField(blank=True, max_length=5, null=True, verbose_name='WT')),
                ('L', models.CharField(blank=True, max_length=9, null=True, verbose_name='L')),
                ('AdjOD', models.CharField(blank=True, max_length=20, null=True, verbose_name='AdjOC')),
                ('AdjID', models.CharField(blank=True, max_length=20, null=True, verbose_name='AdjID')),
                ('AdjWT', models.CharField(blank=True, max_length=20, null=True, verbose_name='AdjWT')),
                ('AdjL', models.CharField(blank=True, max_length=20, null=True, verbose_name='AdjL')),
                ('PipeGrade', models.CharField(blank=True, max_length=50, null=True, verbose_name='Pipe Grade')),
                ('Notes', models.CharField(blank=True, max_length=500, null=True, verbose_name='Notes')),
                ('CoilMaker', models.CharField(blank=True, max_length=50, null=True, verbose_name='Coil Maker')),
                ('CProcess', models.CharField(blank=True, max_length=25, null=True, verbose_name='C Process')),
                ('InBead', models.CharField(blank=True, max_length=10, null=True, verbose_name='InBead')),
                ('SurfLevel', models.CharField(blank=True, max_length=10, null=True, verbose_name='Surface level')),
                ('SurfTreat', models.CharField(blank=True, max_length=20, null=True, verbose_name='Surface Treat')),
                ('Straight', models.CharField(blank=True, max_length=50, null=True, verbose_name='Straight')),
                ('Flaring', models.CharField(blank=True, max_length=50, null=True, verbose_name='Flaring')),
                ('Flattening90', models.CharField(blank=True, max_length=50, null=True, verbose_name='Flattening 90')),
                ('Flattening', models.CharField(blank=True, max_length=50, null=True, verbose_name='Flattening')),
                ('SQWSPost', models.CharField(blank=True, max_length=30, null=True, verbose_name='SQWSPost')),
                ('SQConR', models.CharField(blank=True, max_length=30, null=True, verbose_name='SQConR')),
                ('PPunch', models.CharField(blank=True, max_length=30, null=True, verbose_name='PPunch')),
                ('PackASQty', models.CharField(blank=True, max_length=50, null=True, verbose_name='PackASQty')),
                ('PackPCQty', models.CharField(blank=True, max_length=50, null=True, verbose_name='PackPCQty')),
                ('PackUnit', models.CharField(blank=True, max_length=25, null=True, verbose_name='PackUnit')),
                ('PackASNote', models.CharField(blank=True, max_length=50, null=True, verbose_name='PackASNote')),
                ('PackPCNote', models.CharField(blank=True, max_length=50, null=True, verbose_name='PackPCNote')),
                ('ASPICNote', models.CharField(blank=True, max_length=200, null=True, verbose_name='ASPICNote')),
                ('PipeEdgeValue', models.CharField(blank=True, max_length=5, null=True, verbose_name='PipeEdgeValue')),
                ('PipeEdgeNote', models.CharField(blank=True, max_length=50, null=True, verbose_name='PipeEdgeNote')),
                ('ASManJudgment', models.CharField(blank=True, max_length=15, null=True, verbose_name='ASManJudgment')),
                ('ASManNote', models.CharField(blank=True, max_length=150, null=True, verbose_name='ASManNote')),
                ('ASManDate', models.DateTimeField(blank=True, null=True, verbose_name='ASManDate')),
                ('PIManJudgment', models.CharField(blank=True, max_length=15, null=True, verbose_name='PIManJudgment')),
                ('PIManNote', models.CharField(blank=True, max_length=150, null=True, verbose_name='PIManNote')),
                ('QAManJudgment', models.CharField(blank=True, max_length=15, null=True, verbose_name='QAManJudgment')),
                ('QAManNote', models.CharField(blank=True, max_length=150, null=True, verbose_name='QAManNote')),
                ('QAManDate', models.DateTimeField(blank=True, null=True, verbose_name='QAManDate')),
                ('QCManJudgment', models.CharField(blank=True, max_length=15, null=True, verbose_name='QCManJudgment')),
                ('QCManNote', models.CharField(blank=True, max_length=150, null=True, verbose_name='QCManNote')),
                ('QCManDate', models.DateTimeField(blank=True, null=True, verbose_name='QCManDate')),
                ('PRManJudgment', models.CharField(blank=True, max_length=15, null=True, verbose_name='PRManJudgment')),
                ('PRManNote', models.CharField(blank=True, max_length=150, null=True, verbose_name='PRManNote')),
                ('PRManDate', models.DateTimeField(blank=True, null=True, verbose_name='PRManDate')),
                ('DGDJudgment', models.CharField(blank=True, max_length=15, null=True, verbose_name='DGDJudgment')),
                ('DGDNote', models.CharField(blank=True, max_length=150, null=True, verbose_name='DGDNote')),
                ('DGDManDate', models.DateTimeField(blank=True, null=True, verbose_name='DGDManDate')),
                ('PCManJudgment', models.CharField(blank=True, max_length=15, null=True, verbose_name='PCManJudgment')),
                ('PCManNote', models.CharField(blank=True, max_length=150, null=True, verbose_name='PCManNote')),
                ('PCManDate', models.DateTimeField(blank=True, null=True, verbose_name='PCManDate')),
                ('PIManDate', models.DateTimeField(blank=True, null=True, verbose_name='PCManDate')),
                ('LastUser', models.CharField(blank=True, max_length=500, null=True, verbose_name='LastUser')),
                ('LastimeUser', models.DateTimeField(blank=True, null=True, verbose_name='LastimeUser')),
            ],
        ),
    ]
