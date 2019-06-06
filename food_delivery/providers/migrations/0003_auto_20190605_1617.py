# Generated by Django 2.2.2 on 2019-06-05 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0002_auto_20190605_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurants',
            name='content',
            field=models.TextField(default='none'),
        ),
        migrations.AddField(
            model_name='restaurants',
            name='x',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=9),
        ),
        migrations.AddField(
            model_name='restaurants',
            name='y',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=9),
        ),
    ]