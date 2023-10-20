from django.contrib import admin

# Register your models here.
from .models import Form
 
class FormAdmin(admin.ModelAdmin):
 
    list_display = ("ID","NAME","DATE", "DUE", "FEE", "CONTACT_NO", "EMAIL", "STATUS")

admin.site.register(Form,FormAdmin)
