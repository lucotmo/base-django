from django.test import TestCase

from .models import Categoria, Enlace
from django.contrib.auth.models import User
from django.urls import reverse

class SimpleTest(TestCase):
  def setUp(self):
    self.categoria = Categoria.objects.create(titulo='Categoria de prueba')
    self.usuario = User.objects.create_user(username='carlos', password='password')

  def test_es_popular(self):
    # si un enlace tiene menos de 11 votos no es popular
    enlace = Enlace.objects.create(titulo='Prueba', enlace='https://lucotmo.com', categoria=self.categoria, usuario=self.usuario)
    self.assertEqual(enlace.votos, 0)
    self.assertFalse(enlace.es_popular())

    # si un enlace tiene mas de 11 votos es popular
    enlace.votos = 20
    enlace.save()

    self.assertEqual(enlace.votos, 20)
    self.assertTrue(enlace.es_popular())

  def test_views(self):
    res = self.client.get(reverse('home'))
    self.assertEqual(res.status_code, 200)

    res = self.client.get(reverse('about'))
    self.assertEqual(res.status_code, 200)

    res = self.client.get(reverse('enlaces'))
    self.assertEqual(res.status_code, 200)

    self.assertTrue(self.client.login(username='carlos', password='password'))

    res = self.client.get(reverse('add'))
    self.assertEqual(res.status_code, 200)

  def test_add(self):
    self.assertTrue(self.client.login(username='carlos', password='password'))
    self.assertEqual(Enlace.objects.count(), 0)
    data = {}
    data['titulo'] = 'Test titulo'
    data['enlace'] = 'https://lucotmo.com'
    data['categoria'] = self.categoria.id
    res = self.client.post(reverse('add'), data)
    self.assertEqual(res.status_code, 302)
    self.assertEqual(Enlace.objects.count(), 1)

    enlace = Enlace.objects.all()[0]
    self.assertEqual(enlace.titulo, data['titulo'])
    self.assertEqual(enlace.enlace, data['enlace'])
    self.assertEqual(enlace.categoria, self.categoria)