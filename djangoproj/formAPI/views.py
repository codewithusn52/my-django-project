from django.shortcuts import render
from . import froms
from . import models
# Create your views here.
def create(req):
    if req.method=="POST":
        f= forms.Attendance()
        if f.is_valid():
            models.AttendLogs.object.create(
                empid=f.cleaned_data['empid'],
                fname=f.cleaned_data['fname'],
                lname=f.cleaned_data['lname'],
                shifts=f.cleaned_data['shifts'],
                intime=f.cleaned_data['intime'],
                Action=f.cleaned_data['Action']
            )
        else:
            f = forms.Attendance()
            return render(req,"insert.html",{'form':f})
print("_________________________________________________________________________________________________________________________")

def viewdata(req):
    rec=models.AttendLogs.object.all()
    return render (req,'List.html', {'records':rec})