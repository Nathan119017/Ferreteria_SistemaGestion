# Generated by Django 4.2.10 on 2024-04-29 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsdetail', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsdetail',
            name='precio_unitario',
            field=models.FloatField(blank=True, null=True),
        ),
    ]