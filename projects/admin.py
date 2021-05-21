from django.contrib import admin
from .models import Project

# Register your models here.
# admin.site.register(Project)
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'featured', 'live_site', 'git_repo')
    search_fields = ('title', 'project_detail')
    list_filter = ('featured', 'tags')
    ordering = ('featured', 'date_created')
    prepopulated_fields = {'slug': ('title',)}
