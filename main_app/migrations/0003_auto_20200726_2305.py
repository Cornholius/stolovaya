# Generated by Django 3.0.7 on 2020-07-26 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20200726_2245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='day',
        ),
        migrations.RemoveField(
            model_name='food',
            name='week',
        ),
    ]