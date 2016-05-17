from noticias.models import Noticia, Tag, Imagen
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.forms import modelform_factory
from django.contrib import messages
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import RadioSelect
from django.conf import settings
from django.contrib.auth.decorators import login_required

def vernoticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticias/noticia.html', {'noticias': noticias})

def vernoticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    return render(request, 'noticias/detalle.html', {'noticia':noticia})


def intro_edit_noticia(request, noticia_id=None):
    es_modificacio =(noticia_id!=None)
    noticiaForm =modelform_factory(Noticia,exclude=('id','usuario',))
    if es_modificacio:
        noticia = get_object_or_404(Noticia, id=noticia_id)
    else:
        noticia=Noticia()
    if request.method == 'POST':
        form = noticiaForm(request.POST,request.FILES,instance=noticia)
        if form.is_valid():
            form.instance.usuario = request.user
            noticia = form.save()
            if(es_modificacio):
                messages.add_message(request, messages.SUCCESS, 'Modificado correctamente')
            else:
                messages.add_message(request, messages.SUCCESS, 'Creado correctamente ')
            return HttpResponseRedirect(reverse('noticias:ver_noticias'))
        else:
            if(es_modificacio):
                messages.add_message(request, messages.ERROR, 'Error en la modificacion de la noticia')
            else:
                messages.add_message(request, messages.ERROR, 'Error en crear la noticia')
    else:
        form = noticiaForm(instance=noticia)

    form.helper = FormHelper()
    form.helper.form_class = 'form-horizontal col-md-8 col-md-offset-2'
    form.helper.label_class = 'col-lg-3'
    form.helper.field_class = 'col-lg-8 col-md-8'
    form.helper.add_input(Submit('submit', 'Enviar'))
    return render(request, 'formulario.html', {'form': form, 'noticia':noticia})

def eliminarnoticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    messages.add_message(request, messages.SUCCESS,'La noticia he sido borrado correctamente')
    noticia.delete()
    return HttpResponseRedirect(reverse('noticias:ver_noticias') )

###Tags ###
def vertags(request):
    tags = Tag.objects.all()
    return render(request, 'noticias/tag.html', {'tags': tags})

def intro_edit_tag(request, tag_id=None):
    es_modificacio =(tag_id!=None)
    tagForm =modelform_factory(Tag, exclude=('id',))
    if es_modificacio:
        tag = get_object_or_404(Tag, id=tag_id)
    else:
        tag=Tag()
    if request.method == 'POST':
        form = tagForm(request.POST,request.FILES,instance=tag)
        if form.is_valid():
            tag = form.save()
            if(es_modificacio):
                messages.add_message(request, messages.SUCCESS, 'Modificado correctamente')
            else:
                messages.add_message(request, messages.SUCCESS, 'Creado correctamente ')
            return HttpResponseRedirect(reverse('noticias:ver_tags'))
        else:
            if(es_modificacio):
                messages.add_message(request, messages.ERROR, 'Error en la modificacion del tag')
            else:
                messages.add_message(request, messages.ERROR, 'Error en crear el tag')
    else:
        form = tagForm(instance=tag)

    form.helper = FormHelper()
    form.helper.form_class = 'form-horizontal col-md-6 col-md-offset-3'
    form.helper.label_class = 'col-lg-3'
    form.helper.field_class = 'col-lg-8 col-md-8'
    form.helper.add_input(Submit('submit', 'Enviar'))
    return render(request, 'formulario.html', {'form': form, 'tag':tag})

def eliminartag(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    messages.add_message(request, messages.SUCCESS,'El tag he sido borrado correctamente')
    tag.delete()
    return HttpResponseRedirect(reverse('noticias:ver_tags') )

#imagenes
def verimagenes(request):
    imagenes = Imagen.objects.all()
    return render(request, 'noticias/imagen.html', {'imagenes': imagenes})

def intro_edit_imagen(request, imagen_id=None):
    es_modificacio =(imagen_id!=None)
    imagenForm =modelform_factory(Imagen,exclude=('id','imagen2',))
    if es_modificacio:
        imagen = get_object_or_404(Imagen, id=imagen_id)
    else:
        imagen=Imagen()
    if request.method == 'POST':
        form = imagenForm(request.POST,request.FILES,instance=imagen)
        if form.is_valid():
            imagen = form.save()
            if(es_modificacio):
                messages.add_message(request, messages.SUCCESS, 'Modificado correctamente')
            else:
                messages.add_message(request, messages.SUCCESS, 'Creado correctamente ')
            return HttpResponseRedirect(reverse('noticias:ver_imagenes'))
        else:
            if(es_modificacio):
                messages.add_message(request, messages.ERROR, 'Error en la modificacion de la imagen')
            else:
                messages.add_message(request, messages.ERROR, 'Error en crear la imagen')
    else:
        form = imagenForm(instance=imagen)

    form.helper = FormHelper()
    form.helper.form_class = 'form-horizontal col-md-6 col-md-offset-3'
    form.helper.label_class = 'col-lg-3'
    form.helper.field_class = 'col-lg-8 col-md-8'
    form.helper.add_input(Submit('submit', 'Enviar'))
    return render(request, 'formulario.html', {'form': form, 'imagen':imagen})

def eliminarimagen(request, imagen_id):
    imagen = get_object_or_404(Imagen, pk=imagen_id)
    messages.add_message(request, messages.SUCCESS,'El tag he sido borrado correctamente')
    imagen.delete()
    return HttpResponseRedirect(reverse('noticias:ver_imagenes') )