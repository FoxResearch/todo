# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist
import json
from .models import Usuario, Nota

def index(request):

    nota_list = Nota.objects.filter( publico = True ).order_by('-creado')[:10]
    usuario = request.session.get( 'usuario', 'NONAME' )
    return render( request, 'todo/index.html', {
        'nota_list': nota_list,
        'usuario': usuario
    } )

def login(request):
    usuario = request.session.get('usuario', 'NONAME' )
    if usuario == 'NONAME' or usuario == '':
        return render( request, 'todo/login.html', None )
    return HttpResponseRedirect(reverse('todo:index'))

def loginval(request, accion):
    try:
        o_usuario = Usuario.objects.get(nombreusuario = request.POST['nombreusuario'], password = request.POST['password'] )
    except:
        return render( request, 'todo/login.html', {
            'error_message': "Las credenciales son incorrectas. Por favor vuelva a intentar..."
        })
    else:
        request.session['usuario'] = o_usuario.nombreusuario
        return render( request, 'todo/index.html', context = {
            'nota_list': Nota.objects.filter( publico = True ).order_by('-creado')[:10],
            'usuario': o_usuario.nombreusuario
        } )

def logindel(request):
    del request.session['usuario']
    request.session.modified = True
    return render( request, 'todo/index.html', context = {
        'nota_list': Nota.objects.filter( publico = True ).order_by('-creado')[:10],
        'usuario': 'NONAME'
    } )

def register(request):
    usuario = request.session.get('usuario', 'NONAME' )
    return render( request, 'todo/register.html', context = {
        'usuario': usuario
    } )

def registerval(request, accion):
    try:
        o_usuario = Usuario(
            nombreusuario = request.POST['nombreusuario'],
            password = request.POST['password'],
            nombre = request.POST['nombre'],
            apellido = request.POST['apellido'],
            email = request.POST['email']
        )
        o_usuario.save()
    except:
        return render( request, 'todo/register.html', {
            'error_message': "Los datos son incorrectos. Por favor vuelva a intentar..."
        })
    else:
        request.session['usuario'] = o_usuario.nombreusuario
        return render( request, 'todo/index.html', {
            'nota_list': Nota.objects.filter( publico = True ).order_by('-creado')[:10],
            'usuario': o_usuario.nombreusuario
        } )

def create(request):
    usuario = request.session.get('usuario', 'NONAME' )
    if usuario == 'NONAME' or usuario == '':
        return HttpResponseRedirect(reverse('todo:index'))
    return render( request, 'todo/create.html', { 'usuario' : usuario } )

def createval(request, id):
    usuario = request.session.get('usuario', 'NONAME' )
    if usuario == 'NONAME' or usuario == '':
        return HttpResponseRedirect(reverse('todo:index'))

    pub = True
    try:
        if request.POST['publico'] == None:
            pub = False
    except:
        pub = False

    try:
        o_usuario = Usuario.objects.get(nombreusuario=usuario)
        o_usuario.nota_set.create(texto=request.POST['texto'], titulo=request.POST['titulo'], publico=pub )
    except:
        return render( request, 'todo/create.html', {
            'error_message': 'Error al grabar registro...',
            'usuario': usuario
        } )
    return HttpResponseRedirect(reverse('todo:index'))

def list(request):
    usuario = request.session.get('usuario', 'NONAME' )
    if usuario == 'NONAME' or usuario == '':
        return HttpResponseRedirect(reverse('todo:index'))
    nota_list = Nota.objects.filter( usuario__nombreusuario=usuario ).order_by('-creado')
    return render( request, 'todo/list.html', {
        'nota_list': nota_list,
        'usuario': usuario
    } )

def edit(request, id):
    usuario = request.session.get('usuario', 'NONAME' )
    if usuario == 'NONAME' or usuario == '':
        return HttpResponseRedirect(reverse('todo:index'))
    o_nota = Nota.objects.get(pk=id)
    return render( request, 'todo/edit.html', {
        'nota': o_nota,
        'usuario': usuario
    } )

def editval(request, id):
    usuario = request.session.get('usuario', 'NONAME' )
    if usuario == 'NONAME' or usuario == '':
        return HttpResponseRedirect(reverse('todo:index'))
    ## CODIGO PROPIO
    o_nota = Nota.objects.get(pk=id)

    pub = True
    try:
        if request.POST['publico'] == None:
            pub = False
    except:
        pub = False

    o_nota.texto = request.POST['texto']
    o_nota.titulo = request.POST['titulo']
    o_nota.publico = pub
    o_nota.save()
    ## #################
    nota_list = Nota.objects.filter( usuario__nombreusuario=usuario ).order_by('-creado')
    return render( request, 'todo/list.html', {
        'nota_list': nota_list,
        'usuario': usuario
    } )

def delete(request, id):
    usuario = request.session.get('usuario', 'NONAME' )
    if usuario == 'NONAME' or usuario == '':
        return HttpResponseRedirect(reverse('todo:index'))
    ## CODIGO PROPIO
    o_nota = Nota.objects.get(pk=id)
    o_nota.delete()
    ## #################
    nota_list = Nota.objects.filter( usuario__nombreusuario=usuario ).order_by('-creado')
    return render( request, 'todo/list.html', {
        'nota_list': nota_list,
        'usuario': usuario
    } )

def edituser(request):
    usuario = request.session.get('usuario', 'NONAME' )
    if usuario == 'NONAME':
        return HttpResponseRedirect(reverse('todo:index'))
    o_usuario = Usuario.objects.get(nombreusuario=usuario)
    return render( request, 'todo/edituser.html', {
        'usuario': o_usuario
    } )

def edituserval(request):
    usuario = request.session.get('usuario', 'NONAME' )
    if usuario == 'NONAME':
        return HttpResponseRedirect(reverse('todo:index'))
    o_usuario = Usuario.objects.get(nombreusuario=usuario)
    try:
        o_usuario.password = request.POST['password']
        o_usuario.nombre = request.POST['nombre']
        o_usuario.apellido = request.POST['apellido']
        o_usuario.email = request.POST['email']
        o_usuario.save()
    except:
        return render( request, 'todo/edituser.html', {
            'error_message': "Los datos son incorrectos. Por favor vuelva a intentar...",
            'usuario': o_usuario
        })
    else:
        return HttpResponseRedirect(reverse('todo:index'))
