from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from .models import Categoria, Enlace
from .forms import EnlaceForm
from django.contrib.auth.decorators import login_required

def home(request):
  categorias = Categoria.objects.all()
  enlaces = Enlace.objects.order_by("-votos").all()
  return render(request, 'app/index.html', {'categorias': categorias, 'enlaces': enlaces})

@login_required
def minus(request, id_enlace):
  enlace = Enlace.objects.get(pk=id_enlace)
  enlace.votos = enlace.votos - 1
  enlace.save()
  return redirect('home')

@login_required
def plus(request, id_enlace):
  enlace = Enlace.objects.get(pk=id_enlace)
  enlace.votos = enlace.votos + 1
  enlace.save()
  return redirect('home')

def categoria(request, id_categoria):
  categorias = Categoria.objects.all()
  cat = get_object_or_404(Categoria, pk=id_categoria)
  # cat = Categoria.objects.get(pk=id_categoria)

  enlaces = Enlace.objects.filter(categoria=cat)
  return render(request, 'app/index.html', locals())

@login_required
def add(request):
  if request.method == "POST":
    form = EnlaceForm(request.POST)
    if form.is_valid():
      enlace = form.save(commit=False)
      enlace.usuario = request.user
      enlace.save()
      return redirect('home')
  else:
    form = EnlaceForm()

  return render(request, 'app/form.html', locals())

from django.views.generic import ListView, DetailView

class EnlaceListView(ListView):
  model = Enlace
  context_object_name = 'enlaces'
  def get_template_names(self):
    return 'app/index.html'

class EnlaceDetailView(DetailView):
  model = Enlace
  def get_template_names(self):
    return 'app/index.html'

def hora_actual(request):
  ahora = datetime.now()
  return render(request, 'app/hora.html', {'ahora': ahora, 'usuario': 'Luis Carlos'})
