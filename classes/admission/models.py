from django.db import models

# Create your models here.

class admission_table(models.Model):
    student_id=models.ForeignKey('student_details.student_table',on_delete=models.CASCADE,related_name='student_admissions')
    date=models.DateField()
    course_id=models.ForeignKey('course.course_table',on_delete=models.CASCADE,related_name='course_admissions')
    starttime=models.DateField()
    endtime=models.DateField()
    id_copy=models.CharField(max_length=30)
    fees=models.IntegerField()
    status=models.CharField(max_length=20)
    no_of_days=models.IntegerField()
    remarks=models.TextField()
    pending_fees=models.IntegerField()


    def __str__(self):
        return f"{self.id}-{self.student_id}-{self.course_id}"
