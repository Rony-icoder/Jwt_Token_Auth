from django.contrib import admin
from .models import StudentData,StudentMarks,SubjectDetails

admin.site.register(StudentData)
admin.site.register(SubjectDetails)
admin.site.register(StudentMarks)
