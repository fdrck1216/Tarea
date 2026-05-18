from portafolio.models import Portafolio
from core.models import Persona
from django.shortcuts import render


def obtener_persona():
    return Persona.objects.first()

def home(request):
    return render(request, template_name='core/home.html', context={'persona': obtener_persona()})

def about(request):
    return render(request, template_name='core/about.html', context={'persona': obtener_persona()})

def portafolio(request):
    proyectos = Portafolio.objects.all()
    return render(request, template_name='core/portafolio.html', context={'proyectos': proyectos, 'persona': obtener_persona()})

def contacto(request):
    return render(request, template_name='core/contacto.html', context={'persona': obtener_persona()})