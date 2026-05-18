import os
import django
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_personal.settings')
django.setup()

from portafolio.models import Portafolio

def populate():
    # Ruta donde se guardó la imagen en local
    image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media', 'portafolio', 'spotiwrapped.png')
    
    if not Portafolio.objects.filter(titulo="Spotiwrapped").exists():
        if os.path.exists(image_path):
            p = Portafolio(
                titulo="Spotiwrapped",
                descripcion="Proyecto de seguimiento musical de la música que escuchas a diario, con un resumen semanal, mensual y anual."
            )
            # Guardamos la imagen en el modelo
            with open(image_path, 'rb') as f:
                p.imagem.save('spotiwrapped.png', File(f), save=True)
            print("Proyecto Spotiwrapped agregado correctamente a la base de datos.")
        else:
            print(f"Error: No se encontró la imagen en {image_path}.")
            print("Asegúrate de que la carpeta 'media' y la imagen se hayan subido a PythonAnywhere (revisa que .gitignore no esté bloqueando la subida de la carpeta media).")
    else:
        print("El proyecto Spotiwrapped ya existe en la base de datos.")

if __name__ == '__main__':
    populate()
