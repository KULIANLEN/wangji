# Generated by Django 4.2.5 on 2023-09-21 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='possessions',
            field=models.JSONField(default=[0, 100, 200, 300]),
        ),
    ]
