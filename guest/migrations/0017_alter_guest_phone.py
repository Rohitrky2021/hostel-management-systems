# Generated by Django 4.1.5 on 2023-01-30 17:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0016_alter_guest_first_name_alter_guest_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='phone',
            field=models.CharField(default='+11234567890', max_length=12, validators=[django.core.validators.MinLengthValidator(5)], verbose_name='phone'),
        ),
    ]
