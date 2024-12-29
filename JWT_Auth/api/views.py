from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class StudentView(APIView):
    def get(self,request):
        return Response({"Messgae":"Responce from student get"})

