from django.db import models

# Create your models here.
shifts=(('1','Morning'),
        ('2','Afternoon'),
        ('3','Evening'),
)
class Attendance(models, Model):
    empid=models.CharField(max_length=50,required=True)
    fname=models.CharField(max_length=100,required=True)
    lname=models.CharField(max_length=100,required=True)
    shifts=models.CharField(choices=shifts)
    intime=models.TimeField()#help_text="Enter time in hh:mm format: ")
    Action=models.CharField()
