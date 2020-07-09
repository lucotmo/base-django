"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from app.views import home, plus, minus, categoria, add, EnlaceListView, EnlaceDetailView
from django.views.generic import TemplateView

from rest_framework import routers
from app.views import EnlaceViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'links', EnlaceViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
  re_path(r'^api/', include(router.urls)),
  path('admin/', admin.site.urls),
  path('', home, name='home'),
  re_path(r'^plus/(\d+)$', plus, name='plus'),
  re_path(r'^minus/(\d+)$', minus, name='minus'),
  re_path(r'^categoria/(\d+)$', categoria, name='categoria'),
  re_path(r'^add/', add, name='add'),
  re_path(r'^about/', TemplateView.as_view(template_name="app/index.html"), name='about'),
  re_path(r'^enlaces/', EnlaceListView.as_view() , name='enlaces'),
  re_path(r'^enlaces/(?P<pk>[\d]+)$', EnlaceDetailView.as_view() , name='enlace'),

  re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
