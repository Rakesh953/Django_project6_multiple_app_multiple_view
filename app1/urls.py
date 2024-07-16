from django.urls import path
from app1.views import *
app_name='hey'

urlpatterns=[
    path('app1v1/',app1v1,name='app1v1'),
    path('app1v2/',app1v2,name='app1v2'),
]