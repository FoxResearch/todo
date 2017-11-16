from django.contrib import admin

# Register your models here.
from .models import Usuario, Nota

admin.site.register(Usuario)
admin.site.register(Nota)
