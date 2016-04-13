from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Tag (models.Model):
    nombre_tag = models.CharField(max_length=(100),help_text="Nombre del tag")
    def __str__(self):
        return '%s' % (self.nombre_tag)

class Imagen (models.Model):
    titulo = models.CharField(max_length=100,help_text="El titulo de la imagen")
    imagen = models.ImageField(max_length=200, help_text="Campo Imagen",upload_to='imagenes')

    def __str__(self):
        return '%s' % (self.titulo)

class Noticia (models.Model):
    titulo = models.CharField(max_length=100, help_text="Titulo de la noticia")
    subtitulo = models.CharField(max_length=200, help_text="Subtitulo de la noticia")
    descripcion = models.CharField(max_length=500, help_text="Descripcion de la noticia")
    fecha_publicacion = models.DateField(auto_now=True, help_text="Fecha de publicacion")
    tag = models.ForeignKey(Tag)
    usuario = models.ForeignKey(User)
    imagenes = models.ManyToManyField(Imagen, related_name="noticias")

    def __str__(self):
        return '%s' % (self.titulo)
