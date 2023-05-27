# Generated by Django 3.2.18 on 2023-04-02 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cs', '0019_auto_20230402_0351'),
    ]

    operations = [
        migrations.CreateModel(
            name='pipegrade',
            fields=[
                ('PipeGrade', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Pipe Grade')),
                ('Notes', models.CharField(blank=True, max_length=500, null=True, verbose_name='Note')),
                ('TS', models.CharField(blank=True, max_length=30, null=True, verbose_name='TS')),
                ('YP', models.CharField(blank=True, max_length=30, null=True, verbose_name='YP')),
                ('EL', models.CharField(blank=True, max_length=30, null=True, verbose_name='EL')),
                ('Hardness', models.CharField(blank=True, max_length=30, null=True, verbose_name='Hardness')),
                ('Other', models.CharField(blank=True, max_length=30, null=True, verbose_name='Other')),
                ('ChC', models.CharField(blank=True, max_length=30, null=True, verbose_name='ChC')),
                ('ChSi', models.CharField(blank=True, max_length=30, null=True, verbose_name='ChSi')),
                ('ChMn', models.CharField(blank=True, max_length=30, null=True, verbose_name='ChMn')),
                ('ChP', models.CharField(blank=True, max_length=30, null=True, verbose_name='ChP')),
                ('ChS', models.CharField(blank=True, max_length=30, null=True, verbose_name='ChS')),
                ('ChAL', models.CharField(blank=True, max_length=30, null=True, verbose_name='ChAL')),
                ('ChNi', models.CharField(blank=True, max_length=30, null=True, verbose_name='ChNi')),
                ('ChCr', models.CharField(blank=True, max_length=30, null=True, verbose_name='ChCr')),
                ('ChMo', models.CharField(blank=True, max_length=30, null=True, verbose_name='ChMo')),
                ('ChTi', models.CharField(blank=True, max_length=30, null=True, verbose_name='ChTi')),
                ('ChNb', models.CharField(blank=True, max_length=30, null=True, verbose_name='ChNb')),
                ('ChZr', models.CharField(blank=True, max_length=30, null=True, verbose_name='ChZr')),
                ('ChN', models.CharField(blank=True, max_length=30, null=True, verbose_name='ChN')),
                ('LastUser', models.CharField(blank=True, max_length=50, null=True, verbose_name='LastUser')),
                ('LastimeUser', models.DateTimeField(blank=True, null=True, verbose_name='LastimeUser')),
            ],
        ),
    ]
