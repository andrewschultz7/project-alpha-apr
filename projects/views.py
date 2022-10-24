from django.shortcuts import render
from .models import Project

# Create your views here.


def Project_list(request):
    projectlist = Project.objects.all()
    context = {
        "projectlist_object": projectlist,
    }
    return render(request, "projects/list_projects.html", context)
