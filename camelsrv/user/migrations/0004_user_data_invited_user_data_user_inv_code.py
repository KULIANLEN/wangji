# Generated by Django 4.2.5 on 2023-10-08 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_data_possessions'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_data',
            name='invited',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user_data',
            name='user_inv_code',
            field=models.CharField(default='', max_length=6),
        ),
    ]
