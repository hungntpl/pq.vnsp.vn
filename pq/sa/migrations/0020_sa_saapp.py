# Generated by Django 3.2.18 on 2023-05-12 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sa', '0019_alter_sa_idate'),
    ]

    operations = [
        migrations.AddField(
            model_name='sa',
            name='SAApp',
            field=models.FileField(blank=True, null=True, upload_to='SAApproved/', verbose_name='Approved SA'),
        ),
    ]
