from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm, CarFormWithoutStatus
from django.http import HttpResponse

# Create your views here.
#def home(request):
    #return render(request, "car/home.html" )

#Lista carros p/ admin
def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car/car_list.html', {'cars': cars})
#Cadastro completo p/ admin com status
def car_new(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm()
    return render(request, 'car/car_form.html', {'form': form})


#Cadastro carro sem status para usuario, pq status ativo por padrao
def cadastrar_carro_sem_status(request):
    if request.method == 'POST':
        form = CarFormWithoutStatus(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarFormWithoutStatus()
    return render(request, 'car/car_form_semstatus.html', {'form': form})

#Atualizar carro por id
from django.shortcuts import render, get_object_or_404, redirect
from .models import Car
from .forms import CarForm


#Atualizar Carro
def car_update(request, id):
    car = Car.objects.get(id=id)
    form = CarForm(request.POST or None, instance=car)

    if form.is_valid():
        form.save()
        return redirect('car_list')
    
   
    return render(request, 'car/car_form.html', {'form': form, 'car': car})
    
    
    #return render(request, 'car/car_update.html', {'form': form, 'car': car})



#Deletar carro por id
def car_delete(request, id):
    car = Car.objects.get(id=id)

    if request.method == 'POST':
        car.delete()
        return redirect('car_list')

    return render(request, 'car/car_delete_confirm.html', {'car': car})

#Ver detalhes de cada carro por ID
def car_detail(request, id):
    car = Car.objects.get(id=id)
    return render(request, 'car/car_detail.html', {'car': car})


#View para Exibir toda lista de carros
def car_all_detail(request):
    car = Car.objects.all()

    return render(request, 'car/car_all_detail.html', {'car': car})



