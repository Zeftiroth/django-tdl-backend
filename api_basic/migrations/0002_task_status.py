# Generated by Django 3.1.1 on 2020-09-25 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(default='undone', max_length=255),
        ),
    ]
