from django.db import models

# Create your models here.

class payment_table(models.Model):
    pay_date=models.DateField()
    amount=models.IntegerField()
    type=models.CharField(max_length=10)
    ch_no=models.CharField(max_length=20)
    bank_name=models.CharField(max_length=20)
    branch_name=models.CharField(max_length=20)
    ch_date=models.DateField(null=True)

    def __str__(self):
        return f"{self.pay_date}= {self.amount} --{self.type}"