# Generated by Django 4.2.10 on 2024-04-29 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0017_alter_client_province_alter_product_currency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='paymentTerms',
            field=models.CharField(choices=[('Pago Efectivo', 'Pago Efectivo'), ('Pago Tarjeta', 'Pago Tarjeta'), ('Pago Mixto', 'Pago Mixto')], default='Pago Efectivo', max_length=100),
        ),
    ]