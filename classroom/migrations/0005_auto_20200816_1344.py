# Generated by Django 3.0.3 on 2020-08-16 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0004_auto_20200816_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='invitation_code',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
