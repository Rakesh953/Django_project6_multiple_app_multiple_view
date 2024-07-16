from django.shortcuts import render

# Create your views here.
def app1v1(request):
    return render(request,'app1v1.html')
def app1v2(request):
    return render(request,'app1v2.html') 
