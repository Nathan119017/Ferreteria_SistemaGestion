# Generated by Django 4.2.10 on 2024-04-14 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tax', '0007_rename_fecha_hora_tax_history_fecha_hora'),
    ]

    operations = [
        migrations.AddField(
            model_name='tax_history',
            name='foranea',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tax.tax'),
        ),
    ]