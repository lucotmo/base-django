from django.forms import ModelForm
from .models import *

class EnlaceForm(ModelForm):
  class Meta:
    model = Enlace
    # fields = ['titulo', 'enlace', 'categoria',]
    exclude = ('votos', 'usuario',)