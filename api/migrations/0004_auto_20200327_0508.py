# Generated by Django 3.0.4 on 2020-03-27 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200327_0506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lobby',
            name='session',
            field=models.CharField(default='b05170f2', max_length=7),
        ),
    ]
