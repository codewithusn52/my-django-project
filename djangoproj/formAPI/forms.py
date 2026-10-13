from random import choices
from django import forms

shifts=(('1','Morning'),
        ('2','Afternoon'),
        ('3','Evening'),
)
class Attendance(forms.Form):
    empid=forms.CharField(max_length=50,required=True)
    fname=forms.CharField(max_length=100,required=True)
    lname=forms.CharField(max_length=100,required=True)
    shifts=forms.ChoiceField(choices=shifts)
    intime=forms.TimeField(help_text="Enter time in hh:mm format: ")
    Action=forms.CharField(max_length=50)
