# Generated by Django 3.1.4 on 2020-12-15 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nome_cat',
            field=models.CharField(max_length=60, verbose_name='Categoria'),
        ),
    ]
