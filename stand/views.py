from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages import views
from stand.models import Stand
from .forms import StandForm
from django.core.paginator import Paginator

# Create your views here.

class StandListView(generic.ListView):
  model = Stand
  paginate_by = 1

class StandDetailView(generic.DetailView):
  model = Stand

class StandCreateView(views.SuccessMessageMixin, generic.CreateView):
  model = Stand
  form_class = StandForm
  success_url = reverse_lazy("stand:stand_listar")
  success_message = "Stand cadastrado com sucesso!"
  
class StandDeleteView(views.SuccessMessageMixin, generic.DeleteView):
  model = Stand
  success_url = reverse_lazy("stand:stand_listar")
  success_message = "Stand removido com sucesso!"
  
class StandUpdateView(views.SuccessMessageMixin, generic.UpdateView):
  model = Stand
  form_class = StandForm
  success_url = reverse_lazy("stand:stand_listar")
  success_message = "Stand atualizado com sucesso!"