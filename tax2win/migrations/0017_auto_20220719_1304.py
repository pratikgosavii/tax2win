# Generated by Django 3.0.8 on 2022-07-19 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tax2win', '0016_auto_20220719_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direct_taxcation',
            name='date_time',
            field=models.DateTimeField(),
        ),
    ]
