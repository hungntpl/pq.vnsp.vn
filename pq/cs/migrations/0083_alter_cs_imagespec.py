# Generated by Django 3.2.18 on 2023-05-04 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cs', '0082_alter_cs_packunit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cs',
            name='ImageSPEC',
            field=models.ImageField(blank=True, null=True, upload_to='CSImangeSPEC/', verbose_name='drawing reference'),
        ),
    ]
