# Generated by Django 3.2.18 on 2023-05-13 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('set', '0015_surflevel'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ActionName', models.CharField(blank=True, choices=[('SAAppNote', 'Receive SA approved notice'), ('Other', 'Other notice')], max_length=10, null=True, verbose_name='Action')),
                ('ReciEmail', models.EmailField(max_length=254, verbose_name='Email address of receiver')),
            ],
        ),
    ]