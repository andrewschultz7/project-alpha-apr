from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import CreateTasksForm
from django.contrib.auth.decorators import login_required


@login_required
def create_task(request):
    if request.method == "POST":
        form = CreateTasksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = CreateTasksForm()

    context = {
        "form": form,
    }

    return render(request, "projects/create_task.html", context)


@login_required
def show_task(request):
    assign = Task.objects.filter(assignee=request.user)
    context = {
        "task_assignee": assign,
    }
    return render(request, "mine/show_my_tasks.html", context)
