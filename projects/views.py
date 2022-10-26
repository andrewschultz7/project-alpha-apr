from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from tasks.models import Task
from .forms import CreateProjectForm
from django.contrib.auth.decorators import login_required


@login_required
def list_projects(request):
    projectlist = Project.objects.filter(owner=request.user)
    context = {
        "list_projects": projectlist,
    }
    return render(request, "projects/list_projects.html", context)


@login_required
def show_project(request, id):
    project = get_object_or_404(Project, id=id)
    context = {
        "project_object": project,
    }
    return render(request, "projects/detail.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            receipt = form.save(False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect("list_projects")
    else:
        form = CreateProjectForm()

    context = {
        "form": form,
    }

    return render(request, "projects/create_project.html", context)
