from django.urls import path
from .views import Project_list

urlpatterns = [
    path("projects/", Project_list, name="list_projects"),
]
