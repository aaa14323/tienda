# Generated by Django 4.0.4 on 2022-06-27 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0007_rename_nom_producto_producto_nombre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='producto',
            field=models.ManyToManyField(to='tienda.producto'),
        ),
    ]