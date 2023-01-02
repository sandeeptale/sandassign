from rest_framework import serializers
from .models import EmpAdress
class EmpSerializer(serializers.ModelSerializer):
   class Meta:
       model =EmpAdress
       fields ="__all__"

    
