from django.urls import path
from . import views

from django.urls import path,include
urlpatterns = [
    path('body/',views.body, name='body'),
    path('show/',views.body, name='data'),
    path('',include('Body_para.urls')),

]