# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-12 10:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('titulo', models.CharField(help_text='El titulo de la imagen', max_length=100)),
                ('imagen', models.ImageField(help_text='Campo Imagen', max_length=200, upload_to='imagenes')),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('titulo', models.CharField(help_text='Titulo de la noticia', max_length=100)),
                ('subtitulo', models.CharField(help_text='Subtitulo de la noticia', max_length=200)),
                ('descripcion', models.CharField(help_text='Descripcion de la noticia', max_length=500)),
                ('fecha_publicacion', models.DateField(help_text='Fecha de publicacion')),
                ('imagenes', models.ManyToManyField(null=True, related_name='noticias', to='noticias.Imagen')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('nombre_tag', models.CharField(help_text='Nombre del tag', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='noticia',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noticias.Tag'),
        ),
        migrations.AddField(
            model_name='noticia',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
