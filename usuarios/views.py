from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html') #renderiza arquivo html pra exibir navegador
    elif request.method == "POST":
        return HttpResponse('Teste')
