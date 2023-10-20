from django.contrib import admin

# Register your models here.
from .models import About
 
class LocalAdmin(admin.ModelAdmin):
 
    list_display = ("id", "description")

admin.site.register(About,LocalAdmin)
