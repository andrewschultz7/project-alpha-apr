from django.shortcuts import render
from .models import Project
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def Project_list(request):
    projectlist = Project.objects.filter(owner=request.user)
    context = {
        "projectlist_object": projectlist,
    }
    return render(request, "projects/list_projects.html", context)
