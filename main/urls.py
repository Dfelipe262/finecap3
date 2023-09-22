from django.contrib import admin
from django.urls import path
from reserva.views import ReservaCreateView, ReservaDeleteView, ReservasListView, ReservaUpdateView, ReservaDetailView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ReservasListView.as_view(), name='reserva_listar'),
    path('cadastrar/', ReservaCreateView.as_view(), name='reserva_cadastrar'),
    path('detalhar/<int:pk>/', ReservaDetailView.as_view(), name='reserva_detalhar'),
    path('editar/<int:pk>/', ReservaUpdateView.as_view(), name='reserva_editar'),
    path('deletar/<int:pk>/', ReservaDeleteView.as_view(), name='reserva_deletar'),
      
] + static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

