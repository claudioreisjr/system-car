from django.urls import path
from . import views

app_name = 'car'

urlpatterns = [
    #ESTRUTURA DOS CAMINHOS/DIRETORIOS 
    #lista todos carros cadastrados / no diretorio principal do app car
    #path('', views.car_list, name='car_list'),
    path('detailall/', views.car_list, name='car_list'),
    #cadastra um novo carro
    path('new', views.car_new, name='car_new'),#chama a view que cadastra com imagem car_new

    #cadastrar novo carro sem status, pro usuario
    path('newcar/', views.cadastrar_carro_sem_status, name='car_form_semstatus'),

    #edita um carro por id
    path('edit/<int:id>', views.car_update, name='car_edit'),
    #deletar carro por um id
    path('delete/<int:id>', views.car_delete, name='car_delete'),
    #detalhes de um único carro por um id
    path('detail/<int:id>', views.car_detail, name='car_detail'),
    #detalhes de todos carros
    #path('detailall/', views.car_all_detail, name='car_all_detail'),
    path('', views.car_all_detail, name='car_all_detail'),


] 
