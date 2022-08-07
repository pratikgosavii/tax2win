# Generated by Django 3.0.8 on 2022-07-23 07:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tax2win', '0021_auto_20220721_1812'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_itrdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Unlock_eca',
        ),
        migrations.AddField(
            model_name='file_yourself',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
