from django.db import models

# Create your models here.
class Reviews(models.Model):
    name=models.CharField(max_length=100, verbose_name="Nombre")
    email=models.EmailField(verbose_name="Email")
    message=models.TextField(max_length=500, verbose_name="Comentario")
    image=models.ImageField(verbose_name="Imagen", null=True, blank=True, upload_to="reviews")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    
    class Meta:
        verbose_name="Reseña"
        verbose_name_plural="Reseñas"
        ordering=["-created"]
        
    def __str__(self):
        return self.name + '-' + self.email + '-' + self.message