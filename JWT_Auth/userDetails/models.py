from django.db import models


class DummyData(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    age = models.IntegerField()

    def __str__(self) -> str:
        return self.name