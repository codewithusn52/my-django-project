from django.urls import path
from dtltemp import views
urlpatterns = [
    path('empdetails/',views.emp_port),
]