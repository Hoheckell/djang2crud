from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404,render,redirect
from django.template import loader
from django.http import HttpResponse
from .models import User
from .forms import UserForm,UpdUserForm
from django.contrib import messages

def index(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users':users,'title': 'Usuários'})

def detail(request,id):
    user = get_object_or_404(User, pk=id)
    return render(request, 'detail.html', {'user':user,'title': 'Detalhes do usuário'})

def create(request):
    form = UserForm(request.POST or None)

    if form.is_valid():
        hashed_password = make_password(form.cleaned_data['password'])
        user = User(nome=form.cleaned_data['nome'],email=form.cleaned_data['email'],password=hashed_password)
        user.save()
        messages.success(request, 'Usuário criado com sucesso!')
        return redirect('index')

    return render(request,'new.html',{'form':form,'title':'Novo Cadastro'})

def edit(request,id):

    user = User.objects.filter(id=id).first()
    form = UpdUserForm(instance=user)
    return render(request,'edit.html',{'form':form,'user':user,'title':'Alterar'})

def update(request,id):
    form = UpdUserForm(request.POST or None)

    if form.is_valid():
        user = User.objects.filter(id=id).first()
        user.nome = form.cleaned_data['nome']
        user.email = form.cleaned_data['email']
        user.save()
        messages.success(request, 'Usuário alterado com sucesso!')
        return redirect('index')
    else:
        messages.error(request, 'Dádos inválidos!')
        return redirect('edit_user',id)


def delete(request,id):
    User.objects.filter(id=id).delete()
    return redirect('index')