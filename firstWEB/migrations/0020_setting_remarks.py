# Generated by Django 3.2 on 2021-05-23 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstWEB', '0019_setting'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='remarks',
            field=models.CharField(default='无', max_length=1000),
        ),
    ]
