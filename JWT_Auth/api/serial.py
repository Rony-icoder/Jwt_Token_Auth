from rest_framework import serializers
from .models import StudentData, StudentMarks,SubjectDetails



class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectDetails
        fields = '__all__'
        
class StudentMarkSerializer(serializers.ModelSerializer):

    subject = serializers.CharField(source = "subject.subject")
    class Meta:
        model = StudentMarks
        fields = ["subject", 'mark']



class StudentDataSerializer(serializers.ModelSerializer):

    mark = StudentMarkSerializer(source='studentmarks_set', many=True)
    class Meta:
        model = StudentData
        fields = ["name", "age", 'mark']