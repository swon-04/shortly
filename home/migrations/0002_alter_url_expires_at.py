# Generated by Django 5.0.6 on 2024-06-25 06:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 25, 6, 21, 18, 181222, tzinfo=datetime.timezone.utc)),
        ),
    ]
