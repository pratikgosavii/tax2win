# Generated by Django 3.0.8 on 2022-07-12 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20220712_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]