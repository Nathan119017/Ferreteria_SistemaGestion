# Generated by Django 4.2.10 on 2024-04-13 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='numero_pedido',
            field=models.IntegerField(),
        ),
    ]
