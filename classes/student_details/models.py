from django.db import models

# Create your models here.

class student_table(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    father_fname=models.CharField(max_length=30)
    father_lname=models.CharField(max_length=30)
    building_soc_name=models.CharField(max_length=30)
    house_flat_no=models.CharField(max_length=10)
    landmark=models.CharField(max_length=40)
    area=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    mob_no=models.CharField(max_length=10)
    landline=models.CharField(max_length=8)
    bday=models.DateField()
    gender=models.CharField(max_length=8)
    education=models.CharField(max_length=30)
    institutename=models.CharField(max_length=60)
    email=models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}={self.mob_no}"