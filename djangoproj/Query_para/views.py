from django.shortcuts import render

# Create your views here.
def setform(req):
    return render(req,'index.html')
def getform(req):
    first=req.GET['fname']
    last=req.GET['lname']
    emp={'fn': first,'ln':last}
    return render (req,'view.html',emp)
