from django.shortcuts import render
from . import models # All the files
# From .models import Project, Skill - directly from the 2 files/ of all files with names

def projects_view(request):
  projects_list = models.Project.objects.all().order_by('-year') #All files
  context = {"projects": projects_list}
  #Project.object.all().order_by('-year') - when using the direct name by name

  return render(request, 'projects/projects.html', context)
