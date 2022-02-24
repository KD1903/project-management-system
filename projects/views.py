from django.shortcuts import render, HttpResponse, redirect
from .forms import ProjectForm
from .models import Project

# Create your views here.
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST or None)

        if form.is_valid():
            form.save()
            form = ProjectForm()

    else:
        form = ProjectForm()

    context = {
        'form': form,
    }
    return render(request, 'create_project.html', context)

def view_project(request):
    if request.method == 'GET':
        title = request.GET.get('title')
        
        project = Project.objects.get(title=title)
        
        context = {
            'object': project,
        }

        return render(request, 'view_project.html', context)

def change_tasks(request):
    if request.method == 'POST' or request.method == 'GET':
        form = ProjectForm(request.POST or None)

        titles = request.GET.get('title')
        project = Project.objects.get(title=titles)

        if request.method == 'POST':
            project.pending_tasks = request.POST.get('pending')
            project.working_tasks = request.POST.get('working')
            project.completed_tasks = request.POST.get('completed')
            project.save()
            
            return redirect('dashboard')

        context = {
            'title': project.title,
            'pending_tasks': project.pending_tasks,
            'working_tasks': project.working_tasks,
            'completed_tasks': project.completed_tasks,
        }


    return render(request, 'change_tasks.html', context)
