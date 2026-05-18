from django.db import models

class Portafolio(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()

    imagem = models.ImageField(upload_to='portafolio/', verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    link = models.URLField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ('created',)
        db_table = 'portafolio'


    def __str__(self):
        return self.titulo
