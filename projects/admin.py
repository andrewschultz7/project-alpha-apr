from django.contrib import admin
from .models import Project
from tasks.models import Task

# Register your models here.


@admin.register(Project)
class Project(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
    )


admin.site.register(Task)
