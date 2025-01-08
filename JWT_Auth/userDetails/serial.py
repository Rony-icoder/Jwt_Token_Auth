from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username", "email"]

class RegisterUserSeri(serializers.Serializer):
    username = serializers.CharField()
    email    = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        user = User.objects.create(username = validated_data["username"], email = validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()

        return validated_data
    
class CreateTokenSeri(serializers.Serializer):
    username = serializers.CharField()
    # email    = serializers.EmailField()
    password = serializers.CharField()
