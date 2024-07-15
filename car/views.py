from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm, CarFormWithoutStatus
from django.http import HttpResponse
#para bloquear pagina somente se estiver logado
from django.contrib.auth.decorators import login_required


#teste de tabela Vendidos
from .models import Vendidos

# Create your views here.
#def home(request):
    #return render(request, "car/home.html" )

#Lista carros p/ admin
@login_required
def car_list(request):
    #somente ADMIN vai ter acesso a essa pagina
    if request.user.username != 'admin':
        return redirect('/car')  # Redireciona se o usuário não for 'admin'
    
    cars = Car.objects.all()
    return render(request, 'car/car_list.html', {'cars': cars})
#Cadastro completo p/ admin com status
def car_new(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/car')
    else:
        form = CarForm()
    return render(request, 'car/car_form.html', {'form': form})


#Cadastro carro sem status para usuario, pq status ativo por padrao
#AUTENTICAÇÃO USUARIO NORMAL CLIENTE
@login_required
def cadastrar_carro_sem_status(request):
    if request.method == 'POST':
        form = CarFormWithoutStatus(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/car')
    else:
        form = CarFormWithoutStatus()
    return render(request, 'car/car_form_semstatus.html', {'form': form})

#Atualizar carro por id

def car_update(request, id):
    car = Car.objects.get(id=id)
    form = CarForm(request.POST or None, instance=car)

    if form.is_valid():
        form.save()
        return redirect('/car')
    
    if request.method == "GET":
       return render(request, 'car/car_form.html', {'form': form, 'car': car})
    elif request.method == "POST":
        return HttpResponse('Veículo Atualizado com Sucesso!')
    
    #return render(request, 'car/car_form.html', {'form': form, 'car': car})
    
    
    #return render(request, 'car/car_update.html', {'form': form, 'car': car})



#Deletar carro por id
def car_delete(request, id):
    car = Car.objects.get(id=id)

    if request.method == 'POST':
        car.delete()
        return redirect('/car')

    return render(request, 'car/car_delete_confirm.html', {'car': car})

#Ver detalhes de cada carro por ID
def car_detail(request, id):
    car = Car.objects.get(id=id)
    return render(request, 'car/car_detail.html', {'car': car})

#Ver detalhes de cada carro Vendido por ID
def car_detail_vendido(request, id):
    car = Car.objects.get(id=id)
    return render(request, 'car/car_detail_vendido.html', {'car': car})

#View para Exibir toda lista de carros
def car_all_detail(request):
    car = Car.objects.all()
    return render(request, 'car/car_all_detail.html', {'car': car})


#View para Exibir Veiculos da tabela Car
def vendidos_list(request):
    vendidos = Car.objects.filter(status='vendido')
    return render(request, 'car/vendidos_car.html', {'car': vendidos})

#View para Exibir Veiculos Vendidos (outra tabela)
def vendidos2_list(request):
    vendidos = Vendidos.objects.filter(status='Vendido')
    return render(request, 'car/vendidos_list.html', {'vendidos': vendidos})
