# Generated by Django 3.0.4 on 2020-03-27 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200327_0508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lobby',
            name='session',
            field=models.CharField(default='89962ea5', editable=False, max_length=7),
        ),
    ]
