from django.urls import path
from . import views



app_name = 'car'

urlpatterns = [
    #ESTRUTURA DOS CAMINHOS/DIRETORIOS 
    path('', views.car_list, name='car_list'),
    path('new', views.car_new, name='car_new'),#chama a view que cadastra com imagem car_new
    path('edit/<int:id>', views.car_update, name='car_edit'),
    path('delete/<int:id>', views.car_delete, name='car_delete'),
    
    path('detail/<int:id>', views.car_detail, name='car_detail'),

    #detalhes de todos carros
    path('detailall/', views.car_all_detail, name='car_all_detail'),
] 
