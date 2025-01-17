# Generated by Django 4.2.10 on 2024-04-21 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_users_ihss_users_horario_trabajo_and_more'),
        ('payment_methods', '0002_alter_payment_methods_descripcion_and_more'),
        ('productsdetail', '0001_initial'),
        ('clients', '0002_alter_clients_metodos_pago'),
        ('cai', '0001_initial'),
        ('tax', '0009_delete_tax_history'),
        ('descuentopromotionapp', '0001_initial'),
        ('factura', '0006_alter_factura_notas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='idcai',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='cai.cai'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='idcliente',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='clients.clients'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='iddescuento',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='descuentopromotionapp.promdisc'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='idempleado',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='users.users'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='idmetododepago',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='payment_methods.payment_methods'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='idproductsdetail',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='productsdetail.productsdetail'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='idtax',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='tax.tax'),
        ),
    ]
