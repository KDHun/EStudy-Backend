# Generated by Django 3.0.3 on 2020-08-23 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0008_auto_20200823_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.SmallIntegerField(),
        ),
    ]
