# Generated by Django 3.2 on 2021-05-23 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstWEB', '0020_setting_remarks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='field',
        ),
    ]