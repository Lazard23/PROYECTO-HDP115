# Generated by Django 3.2.4 on 2021-06-23 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_alter_solicitud_pertenece'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='Telefono'),
        ),
        migrations.AlterField(
            model_name='subsidioagua',
            name='cantidad_subsidio',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Cantidad subsidiada'),
        ),
        migrations.AlterField(
            model_name='subsidiogaslicuado',
            name='num_tarjeta',
            field=models.CharField(blank=True, default='-', max_length=10, null=True, verbose_name='Numero tarjeta'),
        ),
    ]
