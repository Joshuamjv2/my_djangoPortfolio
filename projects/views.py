from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Project
from taggit.models import Tag
# Create your views here.

def home(request):
    projects = Project.objects.filter(featured=True).order_by('-date_created')[:3]
    return render(request, 'home/index.html', {'projects':projects})


def all_projects(request, tag_name = None):
    projects = Project.objects.all()
    tag = None
    if tag_name:
        tag = get_object_or_404(Tag, name=tag_name)
        projects = projects.filter(tags__in=[tag])
        print(type(tag))
    return render(request, 'projects/all_projects.html', {'projects':projects, 'tag':tag})