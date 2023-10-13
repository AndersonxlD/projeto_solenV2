from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login
from django.contrib import messages
from django.http.response import Http404, JsonResponse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.shortcuts import get_object_or_404
from django.template import loader
from .forms import ContatoForm, ProdutoModelForm

from .models import Produto

def index(request):
    context = {
        'produtos':Produto.objects.all()
    }
    return render(request, "index.html", context)

def contato(request):
    form = ContatoForm(request.POST or None)
    
    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()
            messages.success(request,'Enviado com sucesso')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar')

    context = {
        'form': form 
    }
    return render(request, "contato.html", context)

def produtos(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():

                form.save()

                messages.success(request, 'Produto salvo com sucesso.')
                form = ProdutoModelForm()
            else:
                messages.error(request, 'Erro ao salvar produto.')
        else:
            form = ProdutoModelForm()
        context = {
            'form': form
        }
        return render(request, 'produtos.html', context)
    else:
        return redirect('index')

def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)