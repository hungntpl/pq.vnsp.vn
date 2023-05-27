# Generated by Django 3.2.18 on 2023-04-02 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cs', '0022_cust'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cs',
            name='CustID',
            field=models.ForeignKey(blank=True, max_length=15, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cs.cust', verbose_name='Cust. ID'),
        ),
    ]
