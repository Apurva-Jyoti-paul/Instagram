# Generated by Django 2.0.2 on 2021-01-29 21:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('photoapp', '0018_auto_20210130_0256'),
    ]

    operations = [
        migrations.CreateModel(
            name='cuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 29, 21, 27, 26, 629021, tzinfo=utc)),
        ),
    ]