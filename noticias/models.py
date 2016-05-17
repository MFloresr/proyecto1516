from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

class Tag (models.Model):
    id = models.AutoField(primary_key = True, unique = True)
    nombre_tag = models.CharField(max_length=(100),help_text="Nombre del tag")
    def __str__(self):
        return '%s' % (self.nombre_tag)

class Imagen (models.Model):
    id = models.AutoField(primary_key = True, unique = True)
    titulo = models.CharField(max_length=100,help_text="El titulo de la imagen")
    imagen = models.ImageField(upload_to='imagenes')
    def __str__(self):
        return '%s' % (self.titulo)

class Noticia (models.Model):
    id = models.AutoField(primary_key = True, unique = True)
    titulo = models.CharField(max_length=100, help_text="Titulo de la noticia")
    subtitulo = models.CharField(max_length=200, help_text="Subtitulo de la noticia")
    entrada = models.CharField(max_length=500, help_text="Frase 1")
    cuerpo = models.TextField(max_length=1000, help_text="Frase 2 o Desarrollo noticia ")
    fecha_publicacion = models.DateTimeField('fecha de publicacion')
    votos = models.IntegerField(default=0)
    tag = models.ForeignKey(Tag)
    usuario = models.ForeignKey(User)
    imagenes = models.ManyToManyField(Imagen, related_name="noticias")
    def __str__(self):
        return '%s' % (self.titulo)

    def publicacion_reciente(self):
        return self.fecha_publicacion >= timezone.now() - datetime.timedelta(days=1)

class Comentario(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    comentario = models.CharField(max_length=500, help_text="Comentario")
    fecha_publicacion = models.DateTimeField('fecha de publicacion')
    usuario = models.ForeignKey(User)
    noticia = models.ForeignKey(Noticia)
    def __str__(self):
        return '%s' % (self.comentario)

    def publicacion_reciente(self):
       return self.fecha_publicacion >= timezone.now() - datetime.timedelta(days=1)