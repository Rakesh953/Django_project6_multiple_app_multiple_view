from django.urls import path
from app3.views import *
app_name='Hii Sir'

urlpatterns=[
    path('app3v1/',app3v1,name='app3v1'),
    path('app3v2/',app3v2,name='app3v2'), 

]