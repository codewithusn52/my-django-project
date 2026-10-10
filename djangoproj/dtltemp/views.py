from django.shortcuts import render

# Create your views here.
def emp_port(req):
    
    emp={'aid':'SCS23','name':'Husna','dept':'Computer Science','age':19,'rep_man':'Mike Carson'}
    skill=['python','HTML','JAVA']
    return render(req,'emp_portfolio.html',{'empdata':emp,'skills':skill})

    
