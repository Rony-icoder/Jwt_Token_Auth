from django.db import models

class StudentData(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    age = models.IntegerField()

    def __str__(self) -> str:
        return self.name

class SubjectDetails(models.Model):
    subject = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.subject
    
class StudentMarks(models.Model):
    name    = models.ForeignKey(StudentData, on_delete=models.CASCADE, to_field='name')
    subject = models.ForeignKey(SubjectDetails, on_delete=models.CASCADE, to_field='subject')
    mark = models.IntegerField()

    def __str__(self):
        return f"{self.name}  {self.subject}   {self.mark}"
    






