# Generated by Django 3.2.7 on 2021-09-26 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starwars', '0002_pelicula_pelicula_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='img',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='personaje',
            name='img',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='planeta',
            name='img',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
