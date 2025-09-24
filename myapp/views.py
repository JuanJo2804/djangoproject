from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    return HttpResponse("Index")


def hello(request, username):
    return HttpResponse(f"Hello {username}, world!")


def project(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)


def task(request, id):
    task = get_object_or_404(Task, id=id)
    return HttpResponse(f'Task: {task.title}')
