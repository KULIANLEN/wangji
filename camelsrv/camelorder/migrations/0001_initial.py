# Generated by Django 4.2.5 on 2023-09-17 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='camel_order',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('items', models.JSONField(default=dict)),
                ('extra', models.JSONField(default=dict)),
                ('status', models.IntegerField(default=0)),
                ('complement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='camelorder.camel_order')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.user_data')),
            ],
        ),
    ]
