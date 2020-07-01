# Generated by Django 3.0.6 on 2020-06-27 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venda', '0002_produto_tipo_de_produto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='produto',
            name='qant',
            field=models.IntegerField(),
        ),
    ]