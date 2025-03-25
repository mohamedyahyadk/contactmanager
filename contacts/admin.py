from django.contrib import admin

# Register your models here.

from .models import Contact ,Registrar ,User

admin.site.register(Contact)
admin.site.register(Registrar)
admin.site.register(User)