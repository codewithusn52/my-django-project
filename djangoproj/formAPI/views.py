from django.shortcuts import render
from . import forms
from . import models
# Create your views here.
def create(req):
    if req.method=="POST":
        f= forms.Attendance()
        if f.is_valid():
            models.AttendLogs.objects.create(
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


def viewdata(req):
    rec=models.AttendLogs.object.all()
    return render (req,'List.html', {'records':rec})


def update(req,id):
    rec=models.AttendLogs.objects.get(id=id)
    if req.method=="POST":
        f= forms.Attendance(req.POST)
        if f.is_valid():
            rec.empid=f.cleaned_data['empid'],
            rec.fname=f.cleaned_data['fname'],
            rec.lname=f.cleaned_data['lname'],
            rec.shifts=f.cleaned_data['shifts'],
            rec.intime=f.cleaned_data['intime'],
            rec.Action=f.cleaned_data['Action']
            rec.save()
    else:
        f=forms.Attendance(initial={
        'empid':rec.empid,
        'fname':rec.fname,
        'lname':rec.lname,
        'shifts':rec.shifts,
        'intime':rec.intime,
        'Action':rec.Action
        })
        return render(req,'Update.html', {'form':f})
    
def delete(req,id):
    rec=models.AttendLogs.objects.get(id=id)
    f=forms.Attendance(req. POST)
    return render (req,'Delete.html',{'form':f})    

