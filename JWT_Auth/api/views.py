from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import APIView


from rest_framework.response import Response
from rest_framework.response import Response

from .serial import StudentDataSerializer
from .serial import StudentDataSerializer

from .models import StudentData
from .models import StudentData


class StudentView(APIView):
    def get(self,request,name=None):
        if name:
            if student := StudentData.objects.filter(name=name).first():
                seri = StudentDataSerializer(student)
            else:
                return Response({"Message":"Student not available"})

        else:
            data = StudentData.objects.all()
            seri = StudentDataSerializer(data, many=True)   
        return Response({"Messgae":"Responce from student get", "Data":seri.data})

