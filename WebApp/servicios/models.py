from distutils.command.upload import upload
from email.headerregistry import ContentDispositionHeader
from tabnanny import verbose
from tkinter import image_names
from urllib import request
from venv import create
from django.db import models

# Create your models here.


class Servicio(models.Model):
   titulo = models.CharField(max_length=50)
   contenido=models.CharField(max_length=50)
   imagen = models.ImageField(upload_to='servicios')
   created=models.DateTimeField(auto_now_add=True)
   updated=models.DateTimeField(auto_now_add=True)

   class Meta:
       verbose_name = 'servicio'
       verbose_name_plural = 'servicios'

   def str(self):
       return self.titulo
