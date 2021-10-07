from functools import update_wrapper
from django.db import models
from django.db.models.deletion import RESTRICT

# Create your models here.
class Empresa(models.Model):
    razonsocial = models.CharField(max_length=200)
    nombrecomercial =  models.CharField(max_length=200)
    ruc =  models.CharField(max_length=11)
    
    def __str__(self):
        return self.razonsocial
    
class Rubro(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre
    
class Especialidad(models.Model):
    rubro = models.ForeignKey(Rubro,on_delete=models.RESTRICT)
    empresa = models.ForeignKey(Empresa,on_delete=RESTRICT)
    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre
    
class Estado(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre
    
class Notificacion(models.Model):
    empresaEmisor = models.OneToOneField(Empresa,on_delete=models.RESTRICT,related_name='emisor')
    empreaReceptor = models.OneToOneField(Empresa,on_delete=models.RESTRICT,related_name='receptor')
    mensaje = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.OneToOneField(Estado,on_delete=RESTRICT)
    
    def __str__(self):
        return self.mensaje
    
class Publicacion(models.Model):
    empresa = models.OneToOneField(Empresa,on_delete=models.RESTRICT,related_name='empresaPublicante')
    mensaje = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='publicaciones',blank=True,null=True)
    estado = models.OneToOneField(Estado,on_delete=RESTRICT)
    
    def __str__(self):
        return self.mensaje
    
class Socio(models.Model):
    empresa = models.OneToOneField(Empresa,on_delete=models.RESTRICT,related_name='titular')
    socio = models.OneToOneField(Empresa,on_delete=models.RESTRICT,related_name='socio')
    estado = models.OneToOneField(Estado,on_delete=RESTRICT)
    
class Visitante(models.Model):
    empresa = models.OneToOneField(Empresa,on_delete=models.RESTRICT,related_name='empresaVisitada')
    visitante = models.OneToOneField(Empresa,on_delete=models.RESTRICT,related_name='visitante')
    fecha = models.DateTimeField(auto_now_add=True)
    
class Requerimiento(models.Model):
    empresa = models.OneToOneField(Empresa,on_delete=models.RESTRICT,related_name='empresaSolicitante')
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='publicaciones',blank=True,null=True)
    estado = models.OneToOneField(Estado,on_delete=RESTRICT)
    
    def __str__(self):
        return self.mensaje
    
class Postulante(models.Model):
    requerimiento = models.ForeignKey(Requerimiento,on_delete=RESTRICT)
    postulante = models.OneToOneField(Empresa,on_delete=models.RESTRICT,related_name='postulante')
    fecha = models.DateTimeField(auto_now_add=True)
    mensaje = models.TextField()
    estado = models.OneToOneField(Estado,on_delete=RESTRICT)
    
    def __str__(self):
        return self.mensaje
    
class Anuncio(models.Model):
    empresa = models.OneToOneField(Empresa,on_delete=models.RESTRICT,related_name='anunciante')
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='publicaciones',blank=True,null=True)
    estado = models.OneToOneField(Estado,on_delete=RESTRICT)
    
    def __str__(self):
        return self.titulo
    

    
