

from django.contrib import admin
from .models import EmpAdress

class adminpanel(admin.ModelAdmin):
   admin.site.register(EmpAdress)

# @admin.register(Student)
# class admindata(admin.ModelAdmin):
#    list_display=  ['stupid','stuname','stupas','Comment']
   
   
   
   
