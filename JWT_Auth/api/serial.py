from rest_framework import serializers
from .models import StudentData, StudentMarks,SubjectDetails
        
class StudentDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentData
        fields = '__all__'

class StudentMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentMarks
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectDetails
        fields = '__all__'
