# Generated by Django 3.0.3 on 2020-08-16 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_auto_20200816_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='invitation_code',
            field=models.CharField(max_length=15),
        ),
    ]
