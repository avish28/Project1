from django.db import models

# Create your models here.

class inquiry_table(models.Model):
    date=models.DateField()
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    second_name=models.CharField(max_length=20)
    st_name=models.CharField(max_length=40)
    area=models.CharField(max_length=40)
    city=models.CharField(max_length=20)
    mob=models.CharField(max_length=10)
    landline=models.CharField(max_length=8)
    collage=models.CharField(max_length=40)
    course_id=models.ForeignKey('course.course_table',on_delete=models.CASCADE,related_name='course_students')
    ref_name=models.CharField(max_length=20)
    remarks=models.TextField()
    inquiry_by=models.CharField(max_length=40)
    type=models.CharField(max_length=20)
    demolec_date=models.DateField()
    demolec_time=models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id}-{self.first_name} course={self.course_id}"