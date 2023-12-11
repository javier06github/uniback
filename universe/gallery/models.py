from django.db import models

# Create your models here.
class project (models.Model):
    title= models.CharField(max_length=200)
    Planet = models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    image = models.ImageField(verbose_name="Imagen",upload_to="projects")
    link= models.URLField(verbose_name="Enlace",null=True,blank=True)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)