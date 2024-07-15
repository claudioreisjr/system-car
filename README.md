# system-car
## Sistema desenvolvido com o Framework django e python3
Front com html, css, bootstrap<br>
Banco de Dados: MySQL, tabelas relacionais<br>


# Servidor: XAMPP para Windows, Apache, MySQL<br>
```sh
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass 
```
Acessar ambiente virtual:<br>
```sh
.\.venv\Scripts\activate   
```
Rodar servidor:<br>
```sh
python manage.py runserver
```
### Estrutura:<br>
APP car<br>
APP usuarios<br>
car inclui todos templates de telas do sistema em geral<br>
usuarios inclui somente templates de Cadastro e Login<br>

SYTEM-CAR<br>
 -car<br>
    -templates<br>
        paginas do sistema em geral<br>
  forms.py<br>
  urls.py<br>
  models.py<br>
  views.py<br>

 -usuarios<br>
    -templates<br>
        -cadastro.html
        -login.html
    urls.py<br>
    models.py<br>
    views.py<br>

## Parte Administrativa e do Usuário:<br>
### Admin:<br>
ipmaquina:porta/urls <br>
http://127.0.0.1:8000/car/detailall  (pode editar, excluir, alterar status)<br>
http://127.0.0.1:80/car/new (para cadastrar um novo veículo)<br>
http://127.0.0.1:8000/car/edit/id (id do veículo para editar detalhes)<br>
http://127.0.0.1:8000/car/delete/id (excluir um veículo pelo seu id)<br>

### Usuário:<br>
http://127.0.0.1:80/car (ver todos veículos cadastrados)<br>
http://127.0.0.1:8000/car/vendidos  (ver veículos vendidos)<br>
http://127.0.0.1:8000/car/detailvenda/id  (ver detalhes de veículos vendidos por id)<br>
http://127.0.0.1:8000/car/detail/7  (ver todos detalhes do veículo pelo id)<br>
http://127.0.0.1:80/car/newcar (para cadastrar um novo veículo sem status)<br>

### Login:<br>
http://127.0.0.1:80/usuarios/cadastro (página de cadastro)<br>
http://127.0.0.1:80/usuarios/login (página de login)<br>
http://127.0.0.1:80/usuarios/sair (deslogar do sistema)<br>
