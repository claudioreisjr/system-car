from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User #importando tabela Usuario do django

#para alerta de mensagens de erro
from django.contrib.messages import constants
from django.contrib import messages

#verificar se existe username e senha no DB
from django.contrib import auth

# view cadastro
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html') #renderiza arquivo html pra exibir navegador
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        
        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, "A senha e confirmar senha devem ser iguais")
            return redirect('/usuarios/cadastro')
        
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, "A senha deve ter mais de 6 digitos")
            return redirect('/usuarios/cadastro')

        users = User.objects.filter(username=username)
         
        #se o usuario ja existe redireciona 
        if users.exists():
            messages.add_message(request, constants.ERROR, "Já existe um usuário com esse username")
            return redirect('/usuarios/cadastro')
        
        try:
            User.objects.create_user(
                username=username,
                email=email,
                password=senha
            )
            return redirect('/usuarios/login')
        except:
            print('Erro 4')
            return redirect('/usuarios/cadastro')
        
        
#view login
def login_view(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        #captar os dados via requisicao HTTP POST 
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        #classe user do django
        #verifica no DB se as credenciais existem
        user = auth.authenticate(request, username=username, password=senha)

        if user: #se existe redireciona pra pagina de cadastrar um veiculo
            auth.login(request, user)  #funcao login requisicao 
            return redirect('/car/newcar/')

        messages.add_message(request, constants.ERROR, 'Usuário ou senha incorretos')
        return redirect('/usuarios/login')
    
#view sair
def sair(request):
    auth.logout(request)
    return redirect('/usuarios/login')


        

