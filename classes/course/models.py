from django.db import models

# Create your models here.

class course_table(models.Model):
    name=models.CharField(max_length=20)
    description=models.TextField()
    duration=models.CharField(max_length=10)
    fees=models.IntegerField()
    status=models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} is {self.status}"