# Generated by Django 3.0.8 on 2022-07-12 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tax2win', '0010_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='mobile',
            new_name='mobile_no',
        ),
    ]
