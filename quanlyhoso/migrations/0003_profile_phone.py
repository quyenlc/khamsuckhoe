# Generated by Django 2.0.4 on 2018-04-05 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quanlyhoso', '0002_auto_20180405_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
