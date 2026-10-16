from django.db import models

# Create your models here.
shifts=(('1','Morning'),
        ('2','Afternoon'),
        ('3','Evening'),
)
class AttendLogs (models.Model):
    empid=models.CharField(max_length=50)
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    shifts=models.CharField(max_length=1,choices=shifts)
    intime=models.TimeField()#help_text="Enter time in hh:mm format: ")
    Action=models.CharField(max_length=50)

def __str__(self):
   return self.empid
