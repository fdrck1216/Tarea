import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_personal.settings')
django.setup()

from core.models import Persona

def populate():
    # If a persona already exists, we could update it, or just create it if there are 0.
    if Persona.objects.exists():
        p = Persona.objects.first()
    else:
        p = Persona()
    
    p.nombres = "Roger Federick"
    p.apellidos = "Sornoza Loaiza"
    p.direccion = "Portoviejo"
    p.telefono = "0963366801"
    p.titulo_academico = "ing. Software"
    p.biografia = "Soy un ingeniero de software apasionado por el desarrollo web y la creación de soluciones tecnológicas innovadoras. A lo largo de mi carrera, he trabajado en diversos proyectos que me han permitido adquirir una sólida experiencia en el ecosistema de Python y tecnologías web."
    p.correo_electronico = "roger.sornoza12@gmail.com"
    p.dedicacion = "ing.software"
    
    p.save()
    print("Persona guardada correctamente.")

if __name__ == '__main__':
    populate()
