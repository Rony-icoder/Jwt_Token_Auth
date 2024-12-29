from django.db import models

class StudentData(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    age = models.IntegerField()

class studentMarks(models.Model):



    