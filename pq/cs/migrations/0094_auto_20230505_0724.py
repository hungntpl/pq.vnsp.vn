# Generated by Django 3.2.18 on 2023-05-05 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cs', '0093_auto_20230505_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cs',
            name='AdjID',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Tol. ID'),
        ),
        migrations.AlterField(
            model_name='cs',
            name='AdjL',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Tol. L'),
        ),
        migrations.AlterField(
            model_name='cs',
            name='AdjOD',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Tol. OD'),
        ),
        migrations.AlterField(
            model_name='cs',
            name='AdjWT',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Tol. WT'),
        ),
    ]