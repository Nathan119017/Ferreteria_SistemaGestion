# Generated by Django 4.2.10 on 2024-04-14 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0004_rename_orders_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_order_cambio', models.CharField(max_length=50)),
                ('nombre_empleado_cambio', models.CharField(max_length=50)),
                ('fecha_de_pedido_cambio', models.CharField(max_length=50)),
                ('metodo_de_pago_cambio', models.CharField(max_length=50)),
                ('estado_pago_cambio', models.CharField(max_length=50)),
                ('estado_pedido_cambio', models.CharField(max_length=50)),
                ('cai_cambio', models.CharField(max_length=50)),
                ('total_cambio', models.CharField(max_length=50)),
                ('Fecha_Hora', models.DateTimeField(auto_now_add=True)),
                ('foranea', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='order.order')),
            ],
        ),
    ]
