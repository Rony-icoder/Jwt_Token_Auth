from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serial import UserSerializer, RegisterUserSeri, CreateTokenSeri
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class RegisterView(APIView):
    def get(self,request):
        data = User.objects.all()
        seri = UserSerializer(data, many=True)
        print(seri.data)

        return Response({"Message":"All user data from registerview", "Data": seri.data})

    def post(self, request):
        data = request.data
        
        seri = RegisterUserSeri(data=data)
         
        if seri.is_valid():
            seri.save()
            
            return Response(seri.data)
        
        return Response({"Error": seri.errors})

class CreateTokenView(APIView):
    def post(self, request):
        data=request.data
        seri = CreateTokenSeri(data=data)
        if not seri.is_valid():
            return Response(seri.errors)
        username = data["username"]
        password = data["password"]
        user = authenticate(request, username = username, password = password)
        if user:
            token = RefreshToken.for_user(user)
            token["username"] = username
            token["scope"] = 'read'

            return Response({"refresh": str(token),
                             "access": str(token.access_token)}) # type: ignore

        return Response({"Messahe":"something is wrong"})

