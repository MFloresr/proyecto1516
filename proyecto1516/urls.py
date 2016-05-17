# encoding: utf-8
from __future__ import unicode_literals

from django.conf.urls import url, include
from django.contrib import admin
from usuarios import views as vista_usuarios
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = ([
    url(r'^admin/', admin.site.urls),
    url(r'^noticias/', include('noticias.urls', namespace='noticias')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^login/', vista_usuarios.vista_login, name="login"),
    url(r'^registrar/', vista_usuarios.registrar, name="registrar"),
    url(r'^sortir/', vista_usuarios.logout_view, name="sortir"  ),

]

    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )