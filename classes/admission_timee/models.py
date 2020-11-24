from django.db import models

# Create your models here.

class ad_time(models.Model):
    admission_id = models.ForeignKey('admission.admission_table', on_delete=models.CASCADE, related_name="ad_time_students")
    start_time=models.CharField(max_length=20)
    end_time=models.CharField(max_length=20)
    date=models.DateField(blank=True)
    remarks=models.TextField()

    def __str__(self):
        return f"{self.id}=={self.date}"
