# Generated by Django 4.2.5 on 2023-09-18 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('camelorder', '0004_alter_camel_order_complement_alter_camel_order_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='cp_inv_code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='camelorder.camel_order')),
            ],
        ),
    ]
