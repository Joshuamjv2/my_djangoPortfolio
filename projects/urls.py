from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.all_projects, name='all-projects'),
    path('projects/<str:tag_name>/', views.all_projects, name='all_projects_by_tagname')
    ]