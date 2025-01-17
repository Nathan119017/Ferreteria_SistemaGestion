# Generated by Django 4.2.10 on 2024-04-14 20:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('descuentopromotionapp', '0001_initial'),
        ('products', '0002_remove_products_id_impuesto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0)),
                ('precio_unitario', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('descripcion', models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(message='El campo no permite caracteres especiales, solo letras y numeros', regex='^[a-zA-Z0-9\\s]+$')])),
                ('precio_final', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('nombre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.products')),
                ('nombrepromocion_descuento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='descuentopromotionapp.promdisc')),
            ],
        ),
    ]
