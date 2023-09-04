from django.shortcuts import render, get_object_or_404, redirect
from .models import Reserva
from .forms import ReservaForm

def listagem(request):
    reservas = Reserva.objects.all()
    return render(request,"listagem.html", {'reservas': reservas})

#cadastrar
def cadastrar_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ReservaForm()      
    else:
        form = ReservaForm()
    
    return render(request, "form.html", {'form':form})

#detalhar
def detalhar(request, id):
    reservas = get_object_or_404(Reserva,id=id)
    return render(request,'detalhar.html', {'reservas': reservas})

#editar
def editar(request, id):
    reserva = get_object_or_404(Reserva, id=id)

    if request.method =='POST':
        form = ReservaForm(request.POST,request.FILES,instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = ReservaForm(instance=reserva)

    return render(request,'form.html',{'form':form})
        
#deletar
def deletar(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect('listar')
