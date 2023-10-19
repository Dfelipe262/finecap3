from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages import views
from reserva.models import Reserva
from .forms import ReservaForm
from django.core.paginator import Paginator

# Create your views here.

class ReservasListView(generic.ListView):
  model = Reserva
  paginate_by = 1

class ReservaDetailView(generic.DetailView):
  model = Reserva

class ReservaCreateView(views.SuccessMessageMixin, generic.CreateView):
  model = Reserva
  form_class = ReservaForm
  success_url = reverse_lazy("reserva:reserva_listar")
  success_message = "Reserva cadastrada com sucesso!"
  
class ReservaDeleteView(views.SuccessMessageMixin, generic.DeleteView):
  model = Reserva
  success_url = reverse_lazy("reserva:reserva_listar")
  success_message = "Reserva removida com sucesso!"
  
class ReservaUpdateView(views.SuccessMessageMixin, generic.UpdateView):
  model = Reserva
  form_class = ReservaForm
  success_url = reverse_lazy("reserva:reserva_listar")
  success_message = "Reserva atualizada com sucesso!"
