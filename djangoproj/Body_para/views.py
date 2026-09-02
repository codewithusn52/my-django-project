from django.shortcuts import render

# Create your views here.
def body(req):
    return render(req,'Body_para/index.html')

def showdata(req):
    first=req.POST['fn']
    last=req.POST['ln']
    emp={'fname':first,'lname':last}
    return render(req,'Body_para/show.html',emp)
