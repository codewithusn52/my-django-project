from django.shortcuts import render

# Create your views here.
def index1(req):
    return render(req,'index1.html')