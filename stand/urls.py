from django.urls import path

from . import views

app_name = "stand"
urlpatterns = [
    path('stand/list', views.StandListView.as_view(), name='stand_listar'),
    path('stand/detail/<int:pk>/', views.StandDetailView.as_view(), name='stand_detalhar'),
    path('stand/update/<int:pk>/', views.StandUpdateView.as_view(), name='stand_editar'),
    path('stand/delete/<int:pk>/', views.StandDeleteView.as_view(), name='stand_deletar'),
    path('stand/create/', views.StandCreateView.as_view(), name='stand_cadastrar'),
]