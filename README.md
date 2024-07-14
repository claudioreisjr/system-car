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


### Admin:<br>
ipmaquina:porta/urls <br>
http://127.0.0.1:80/car (home para ver lista de veículos cadastrados)<br>
http://127.0.0.1:80/car/new (para cadastrar um novo veículo)<br>
http://127.0.0.1:8000/car/edit/13 (id do veículo para editar detalhes)<br>
http://127.0.0.1:8000/car/delete/6 (excluir um veículo pelo seu id)<br>

### Usuário:<br>
http://127.0.0.1:80/car/detailall  (ver todos veiculos em formato de card)<br>
http://127.0.0.1:8000/car/detail/7  (ver todos detalhes do veículo pelo id)<br>
