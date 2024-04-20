from django.shortcuts import render
from .models import Especialidades
from django.http import HttpResponse
# Create your views here.

def cadastro_medico(request):
    if request.method == "GET":
        especialidades = Especialidades.objects.all()
        return render(request, 'cadastro_medico.html',{'especialidades': especialidades})
    elif request.method == "POST":
        return 
