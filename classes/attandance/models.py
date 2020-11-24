from django.db import models

# Create your models here.

class attandance_table(models.Model):
    admission_id = models.ForeignKey('admission.admission_table', on_delete=models.CASCADE,
                                     related_name="students")
    date=models.DateField()
    status=models.CharField(max_length=10)
    remarks=models.TextField()
    time=models.CharField(max_length=10)

    def __str__(self):
        return f"{self.admission_id}-->{self.status}"