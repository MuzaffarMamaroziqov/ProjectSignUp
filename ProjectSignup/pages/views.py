from django.shortcuts import render

def Blog(request):
    return render(request,'pages/home.html')

def Backup(request):
    return render(request,'pages/content.html')

# Create your views here.
