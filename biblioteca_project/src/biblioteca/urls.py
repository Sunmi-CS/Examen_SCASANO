from django.test import TestCase

from django.urls import path
from . import views


urlpatterns = [
    path('', views.lista_libros, name='lista_libros'),
]
