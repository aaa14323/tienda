# Generated by Django 4.0.4 on 2022-06-21 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='imagen_p',
        ),
    ]
