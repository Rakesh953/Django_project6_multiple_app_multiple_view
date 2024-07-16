from django.urls import path
from app2.views import *
app_name='Hii Sir'

urlpatterns=[
    path('app2v1/',app2v1,name='app2v1'),
    path('app2v2/',app2v2,name='app2v2'), 

]