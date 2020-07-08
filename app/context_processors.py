from random import choice
frases = ['Lucho es un gran diseñador', 'Lucotmo es fullStack', 'Luchotero super Fotografo']

def ejemplo(request):
  return {'frase': choice(frases)}

from django.urls import reverse

def menu(request):
  menu = {'menu': [
    {'name': 'Home', 'url': reverse('home')},
    {'name': 'Add', 'url': reverse('add')},
    {'name': 'About', 'url': reverse('about')},
  ]}
  for item in menu['menu']:
    if request.path == item['url']:
      item['active'] = True
  return menu