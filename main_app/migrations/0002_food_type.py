# Generated by Django 3.0.7 on 2020-06-11 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='type',
            field=models.CharField(choices=[('123', '456'), ('2121', '3231')], default='', max_length=20),
        ),
    ]
