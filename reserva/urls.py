from django.urls import path

from . import views

app_name = "reserva"
urlpatterns = [
    path('', views.ReservasListView.as_view(), name='reserva_listar'),
    path('reservas/detail/<int:pk>/', views.ReservaDetailView.as_view(), name='reserva_detalhar'),
    path('reservas/update/<int:pk>/', views.ReservaUpdateView.as_view(), name='reserva_editar'),
    path('reservas/delete/<int:pk>/', views.ReservaDeleteView.as_view(), name='reserva_deletar'),
    path('reservas/create/', views.ReservaCreateView.as_view(), name='reserva_cadastrar'),
]