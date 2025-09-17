from django.shortcuts import render
from .models import Libros

def lista_libros(request):
    libros = Libros.objects.all()
    return render(request, 'libros/libros_list.html', {'libros': libros})


