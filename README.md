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
# Estrutura do Projeto SYSTEM-CAR

### `car`
Este diretório inclui todos os templates e arquivos relacionados às funcionalidades gerais do sistema.

- **templates/paginas do sistema em geral**: Contém os templates HTML para as páginas gerais do sistema.
- **forms.py**: Define os formulários utilizados no aplicativo `car`.
- **urls.py**: Configura as URLs específicas do aplicativo `car`.
- **models.py**: Define os modelos de dados do aplicativo `car`.
- **views.py**: Contém as views que controlam as funcionalidades e a lógica de apresentação das páginas do aplicativo `car`.

### `usuarios`
Este diretório inclui os templates e arquivos relacionados ao cadastro e login de usuários.

- **templates/cadastro.html**: Template HTML para a página de cadastro de usuários.
- **templates/login.html**: Template HTML para a página de login de usuários.
- **urls.py**: Configura as URLs específicas do aplicativo `usuarios`.
- **models.py**: Define os modelos de dados do aplicativo `usuarios`.
- **views.py**: Contém as views que controlam as funcionalidades e a lógica de apresentação das páginas de cadastro e login de usuários.


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
