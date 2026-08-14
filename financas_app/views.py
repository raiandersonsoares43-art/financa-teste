from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Transacao
from .forms import TransacaoForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    transacoes = Transacao.objects.filter(usuario=request.user).order_by('-data')
    
    # Cálculos
    total_entradas = sum(t.valor for t in transacoes if t.tipo == 'RECEITA')
    total_saidas = sum(t.valor for t in transacoes if t.tipo == 'DESPESA')
    saldo = total_entradas - total_saidas
    
    return render(request, 'dashboard.html', {
        'transacoes': transacoes,
        'total_entradas': total_entradas,
        'total_saidas': total_saidas,
        'saldo': saldo,
    })

@login_required
def nova(request):
    if request.method == 'POST':
        form = TransacaoForm(request.POST)
        if form.is_valid():
            transacao = form.save(commit=False)
            transacao.usuario = request.user
            transacao.save()
            messages.success(request, 'Transação adicionada com sucesso!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Corrija os erros abaixo.')
    else:
        form = TransacaoForm()
    
    return render(request, 'nova.html', {'form': form})

@login_required
def excluir(request, id):
    transacao = get_object_or_404(Transacao, id=id, usuario=request.user)
    transacao.delete()
    messages.success(request, 'Transação excluída com sucesso!')
    return redirect('dashboard')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'login.html')

def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Corrija os erros abaixo.')
    else:
        form = UserCreationForm()
    
    return render(request, 'registro.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')