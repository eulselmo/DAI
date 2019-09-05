# restaurantes/urls.py

from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^index/$', views.index, name='index'),
  url(r'^fotos/$', views.fotos, name='fotos'),
  url(r'^buscar/$', views.buscar, name='buscar'),
  url(r'^introducir/$', views.nuevo_restaurante, name='introducir'),
  url(r'^datos/$', views.datos, name='datos'),
  url(r'^editar/$', views.editar, name='editar'),
  url(r'^grafica/$', views.grafica, name='grafica'),
  url(r'^test_template/$', views.test_template, name='test_template'),
  url(r'^get_name/$', views.get_name, name='get_name'),
]
