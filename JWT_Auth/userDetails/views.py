from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User


class RegisterView(APIView):
    def get(self,request):
        return Response({"Message":"All user data from registerview"})

    def post(self, request):
        return Response({"Message":"Register New User"})



