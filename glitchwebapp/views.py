from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def projects(request):
    return render(request, 'projects.html')

def internship(request):
    return render(request, 'internship.html')

def join(request):
    return render(request, 'join.html')

def about(request):
    return render(request, 'about.html')
