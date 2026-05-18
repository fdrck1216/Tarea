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
    import shutil
    import os
    from portafolio.models import Portafolio
    
    src_img = r"C:\Users\Roger\.gemini\antigravity\brain\4f12ce5a-3475-40ee-b47b-5732b6ba6c24\spotiwrapped_mockup_1779067125819.png"
    dst_dir = r"c:\Users\Roger\Desktop\webtarea\web_personal_roger_sornoza\media\portafolio"
    os.makedirs(dst_dir, exist_ok=True)
    dst_img = os.path.join(dst_dir, "spotiwrapped.png")
    
    try:
        shutil.copy(src_img, dst_img)
        if not Portafolio.objects.filter(titulo="Spotiwrapped").exists():
            Portafolio.objects.create(
                titulo="Spotiwrapped",
                descripcion="Proyecto de seguimiento musical de la música que escuchas a diario, con un resumen semanal, mensual y anual.",
                imagem="portafolio/spotiwrapped.png"
            )
    except Exception as e:
        print("Error adding project:", e)

    proyectos = Portafolio.objects.all()
    return render(request, template_name='core/portafolio.html', context={'proyectos': proyectos, 'persona': obtener_persona()})

def contacto(request):
    return render(request, template_name='core/contacto.html', context={'persona': obtener_persona()})