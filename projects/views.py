from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Project
# Create your views here.

def home(request):
    projects = Project.objects.filter(featured=True)
    return render(request, 'home/index.html', {'projects':projects})


def all_projects(request):
    projects = Project.objects.filter(featured=True)
    return render(request, 'project.html', {'projects':projects})