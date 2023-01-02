from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from .models import EmpAdress
from .serializers import EmpSerializer
# from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
# from datetime import datetime
# import pytz



# class EmpListCreate(ListCreateAPIView):
#     queryset = EmpAdress.objects.all()
#     serializer_class = EmpSerializer
    


# class EmpRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
#     queryset =EmpAdress.objects.all()
#     serializer_class = EmpSerializer
# success_message = "Post was created successfully"
   
   
    
@api_view(['GET', 'POST', ])
def Emp_api(request):
    if request.method == 'GET':
       id = request.GET.get('id')
       if id is not None:
           emp = EmpAdress.objects.get(id=id)
           serializer  = EmpSerializer(emp)
           return Response(serializer.data)
       
       emp = EmpAdress.objects.all()
       serializer = EmpSerializer(emp, many=True)
       return Response(serializer.data)
   
    if request.method == 'POST':
        serializer = EmpSerializer(data=request.data)
      

        
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' :'Submitted'})
        return Response(serializer.errors)