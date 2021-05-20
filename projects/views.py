from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Project
# Create your views here.

def home(request):
    return render(request, 'home/index.html')


def all_projects(request):
    projects = Project.objects.all()
    return render(request, 'project.html', {'projects':projects})