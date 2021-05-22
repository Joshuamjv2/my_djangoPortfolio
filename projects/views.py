from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Project
from taggit.models import Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def home(request):
    projects = Project.objects.filter(featured=True).order_by('-date_created')[:3]
    return render(request, 'home/index.html', {'projects':projects})


def all_projects(request, tag_name = None):
    project_list = Project.objects.all()
    tag = None
    if tag_name:
        tag = get_object_or_404(Tag, name=tag_name)
        project_list = project_list.filter(tags__in=[tag])
        print(type(tag))
    paginator = Paginator(project_list, 4)
    page = request.GET.get('page')
    try:
        projects  = paginator.page(page)
    except  PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)
    return render(request, 'projects/all_projects.html', {'projects':projects, 'tag':tag})
