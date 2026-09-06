"""from django.shortcuts import render

# Create your views here.
def setform(req):
    return render(req,'index.html')
def getform(req):
    first=req.GET['fn']
    last=req.GET['ln']
    emp={'fn': first,'ln':last}
    return render (req,'view.html',emp)"""
