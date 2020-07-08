from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from random import choice

paises = ['Colombia', 'Peru', 'Panama', 'Mexico']

def de_donde_vengo(request):
  # return 'Colombia'
  return choice(paises)

class PaisMiddleware(MiddlewareMixin):
  def process_request(self, request):
    pass
    # pais = de_donde_vengo(request)
    # if pais == 'Mexico':
    #   return redirect('https://lucotmo.com')
