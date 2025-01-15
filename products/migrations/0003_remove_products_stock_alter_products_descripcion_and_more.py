# Generated by Django 4.2.10 on 2024-04-14 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0002_alter_suppliers_apellido_and_more'),
        ('products', '0002_remove_products_id_impuesto_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='stock',
        ),
        migrations.AlterField(
            model_name='products',
            name='descripcion',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='products',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='products',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='suppliers.suppliers'),
        ),
    ]