# Generated by Django 3.0.4 on 2020-03-27 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200327_0516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lobby',
            name='moves',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Moves'),
        ),
    ]