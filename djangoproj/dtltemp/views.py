from django.shortcuts import render

# Create your views here.
def emp_port(req):
    
    emp={'aid':'SCS52','name':'Husna Shaikh','dept':'Computer Science','age':19,'rep_man':'Mike Carson'}
    skill=['Python Programming','HTML','JAVA Programming ']
    return render(req,'emp_protfolio.html',{'empdata':emp,'skills':skill})

    
