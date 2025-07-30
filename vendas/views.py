from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from .models import Carro, Compra
from .forms import CarroForm

def home(request):
    carros = Carro.objects.filter(disponivel=True).order_by('-data_cadastro')[:6]
    return render(request, 'home.html', {'carros': carros})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha incorretos!')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso! Faça login para continuar.')
            return redirect('login')
        else:
            messages.error(request, 'Erro ao criar conta. Verifique os dados.')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def carros_list(request):
    query = request.GET.get('q', '')
    marca = request.GET.get('marca', '')
    preco_min = request.GET.get('preco_min', '')
    preco_max = request.GET.get('preco_max', '')
    
    carros = Carro.objects.filter(disponivel=True)
    
    if query:
        carros = carros.filter(
            Q(marca__icontains=query) | 
            Q(modelo__icontains=query) | 
            Q(descricao__icontains=query)
        )
    
    if marca:
        carros = carros.filter(marca=marca)
    
    if preco_min:
        carros = carros.filter(preco__gte=preco_min)
    
    if preco_max:
        carros = carros.filter(preco__lte=preco_max)
    
    carros = carros.order_by('-data_cadastro')
    
    context = {
        'carros': carros,
        'marcas': Carro.MARCA_CHOICES,
        'query': query,
        'marca_filtro': marca,
        'preco_min': preco_min,
        'preco_max': preco_max,
    }
    return render(request, 'carros_list.html', context)

def carro_detail(request, carro_id):
    carro = get_object_or_404(Carro, id=carro_id)
    return render(request, 'carro_detail.html', {'carro': carro})

@login_required
def comprar_carro(request, carro_id):
    carro = get_object_or_404(Carro, id=carro_id, disponivel=True)
    
    if request.method == 'POST':
        # Verificar se o carro ainda está disponível
        if carro.disponivel:
            # Criar a compra
            compra = Compra.objects.create(
                comprador=request.user,
                carro=carro,
                preco_pago=carro.preco
            )
            
            # Marcar o carro como indisponível
            carro.disponivel = False
            carro.save()
            
            messages.success(request, f'Parabéns! Você comprou o {carro}!')
            return redirect('minhas_compras')
        else:
            messages.error(request, 'Este carro já não está mais disponível.')
    
    return render(request, 'comprar_carro.html', {'carro': carro})

@login_required
def minhas_compras(request):
    compras = Compra.objects.filter(comprador=request.user).order_by('-data_compra')
    return render(request, 'minhas_compras.html', {'compras': compras})

@login_required
def perfil(request):
    return render(request, 'perfil.html')
