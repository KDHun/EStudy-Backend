# Generated by Django 3.0.3 on 2020-08-23 08:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0006_gradedassignment'),
    ]

    operations = [
        migrations.AddField(
            model_name='gradedassignment',
            name='submitted',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
