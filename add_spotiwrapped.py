import os
import django
import shutil

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_personal.settings")
django.setup()

from portafolio.models import Portafolio
from django.core.files import File

# Copy image first
src_img = r"C:\Users\Roger\.gemini\antigravity\brain\4f12ce5a-3475-40ee-b47b-5732b6ba6c24\spotiwrapped_mockup_1779067125819.png"
dst_dir = os.path.join("media", "portafolio")
os.makedirs(dst_dir, exist_ok=True)
dst_img = os.path.join(dst_dir, "spotiwrapped.png")
shutil.copy(src_img, dst_img)

Portafolio.objects.create(
    titulo="Spotiwrapped",
    descripcion="Proyecto de seguimiento musical de la música que escuchas a diario, con un resumen semanal, mensual y anual.",
    imagem="portafolio/spotiwrapped.png"
)

print("Spotiwrapped added successfully.")
