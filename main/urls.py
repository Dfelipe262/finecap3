from django.contrib import admin
from django.urls import path
from reserva.views import listagem, cadastrar, detalhar, editar, deletar
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listagem, name='listagem'),
    path('cadastrar/', cadastrar, name='cadastrar'),
    path('detalhar/<int:id>/', detalhar, name='detalhar'),
    path('editar/<int:id>/', editar, name='editar'),
    path('deletar/<int:id>/', deletar, name='deletar'),
      
] + static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
