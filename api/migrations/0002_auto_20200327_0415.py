# Generated by Django 3.0.4 on 2020-03-27 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lobby',
            name='Session',
            field=models.UUIDField(default='c4bd32f1', editable=False),
        ),
    ]
