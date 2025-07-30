from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('carros/', views.carros_list, name='carros_list'),
    path('carro/<int:carro_id>/', views.carro_detail, name='carro_detail'),
    path('comprar/<int:carro_id>/', views.comprar_carro, name='comprar_carro'),
    path('minhas-compras/', views.minhas_compras, name='minhas_compras'),
    path('perfil/', views.perfil, name='perfil'),
] 