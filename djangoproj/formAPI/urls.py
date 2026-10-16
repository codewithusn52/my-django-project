from django.contrib import admin
from django.urls import path 
from formAPI import views
from . import views

urlpatterns=[
    path('admin/',admin.site.urls),
    path('insert/',views.create,name='create'),
    path('List/',views.viewdata,name='list'),
    path('Update/<int:id>',views.update,name='update'),
    path('Delete/<int:id>',views.delete,name='delete'),
]