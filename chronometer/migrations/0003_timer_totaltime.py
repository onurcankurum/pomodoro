# Generated by Django 3.1.3 on 2020-12-10 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chronometer', '0002_segment_onfocus'),
    ]

    operations = [
        migrations.AddField(
            model_name='timer',
            name='totalTime',
            field=models.DurationField(null=True),
        ),
    ]
