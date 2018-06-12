from django.shortcuts import render
from apps.Investigador.models import Investigador
from apps.roles.models import Rol
# Create your views here.
def inde(request):
    return render(request, 'Home/inicio.html')

def producc(request):
    return render(request, 'Home/produccioncientifica.html')

def similar(request):
    perfil = Investigador.objects.all()
    privi = []
    for p in perfil:
        if p.roles == '3':
            privi.append(p)

    return render(request, 'Home/similares.html',{'usuario': perfil})