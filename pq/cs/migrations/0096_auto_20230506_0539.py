# Generated by Django 3.2.18 on 2023-05-06 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cs', '0095_auto_20230506_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csapproved',
            name='CSNo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cs.cs', verbose_name='CS No'),
        ),
        migrations.AlterField(
            model_name='cspi',
            name='CSNo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cs.cs', verbose_name='CS No'),
        ),
    ]
