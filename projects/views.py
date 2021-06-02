# inbuilt
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
# local project files
from .forms import ContactForm
from .models import Project
# more functionality files
from taggit.models import Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail, get_connection



def home(request):
    projects = Project.objects.filter(featured=True).order_by('-date_created')[:3]
    submitted = False
    # if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         cd = form.cleaned_data
    #         con = get_connection('django.core.mail.backends.console.EmailBackend')
    #         send_mail(
    #             cd['full_name'],
    #             cd['message'][:50].replace('\n', ' ').replace('\t', '').replace('\r', ''),
    #             cd.get('email'),
    #             ['myportfolio@example.com'],
    #             fail_silently=False,
    #             connection=con
    #         )
    #         return HttpResponseRedirect('/?submitted=True')
    #     else:
    #         print(form.errors)
    # else:
    #     form = ContactForm()
    #     if 'submitted' in request.GET:
    #             submitted = True
    # return render(request, 'home/index.html', {'form':form, 'submitted':submitted,'projects':projects})
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


def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            cd = form.cleaned_data
            # con = get_connection('django.core.mail.backends.console.EmailBackend')
            body = {
                'full_name': 'Name: ' + cd['full_name'],
                'message': 'Message: '+cd['message'].replace('\n', ' ').replace('\t', '').replace('\r', ''),
                'email': 'Email: ' + cd['email']
            }
            message = "\n\n".join(body.values())
            send_mail(
                cd['full_name'],
                message,
                'joshuamjv22@gmail.com',
                ['joshuamjv22@gmail.com',],
                fail_silently=False,
                # connection=con
            )
            return HttpResponseRedirect('/contact?submitted=True')
        # else:
        #     # form = ContactForm()
        #     print(form.errors)
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
                submitted = True
    return render(request, 'contact/contact.html', {'form':form, 'submitted':submitted})