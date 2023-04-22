# Generated by Django 4.1.5 on 2023-01-30 16:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0013_alter_room_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='phone',
            field=models.CharField(blank=True, max_length=12, null=True, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]