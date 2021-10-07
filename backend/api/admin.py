from django.contrib import admin

# Register your models here.
from .models import Empresa,Rubro,Especialidad,Notificacion,Estado

admin.site.register(Empresa)
admin.site.register(Rubro)
admin.site.register(Especialidad)
admin.site.register(Notificacion)
admin.site.register(Estado)
