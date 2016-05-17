from django.conf.urls import url
from . import views

urlpatterns = [

    # ex: /noticias/
    url(r'^$', views.vernoticias, name='ver_noticias'),
     # ex: /noticias/5/
    url(r'^(?P<noticia_id>[0-9]+)/$', views.vernoticia, name='ver_noticia'),
    url(r'^introduirnoticia/$', views.intro_edit_noticia, name='nueva_noticia'),
    url(r'^editarnoticia/(?P<noticia_id>[0-9]+)/$', views.intro_edit_noticia, name='editar_noticia'),
    url(r'^eliminarnoticia/(?P<noticia_id>[0-9]+)/$', views.eliminarnoticia, name='eliminar_noticia'),

    #tags
    url(r'^tags/$', views.vertags, name='ver_tags'),
    url(r'^introduirtag/$', views.intro_edit_tag, name='nuevo_tag'),
    url(r'^editartag/(?P<tag_id>[0-9]+)/$', views.intro_edit_tag, name='editar_tag'),
    url(r'^eliminartag/(?P<tag_id>[0-9]+)/$', views.eliminartag, name='eliminar_tag'),

    #imagenes
    url(r'^imagenes/$', views.verimagenes, name='ver_imagenes'),
    url(r'^introduirimagen/$', views.intro_edit_imagen, name='nueva_imagen'),
    url(r'^editarimagen/(?P<imagen_id>[0-9]+)/$', views.intro_edit_imagen, name='editar_imagen'),
    url(r'^eliminarimagen/(?P<imagen_id>[0-9]+)/$', views.eliminarimagen, name='eliminar_imagen'),
]