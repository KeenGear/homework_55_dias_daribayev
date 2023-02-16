from django.shortcuts import render, redirect, get_object_or_404
from .models import Tasks
from .forms import TasksForm


# Create your views here.

def task_list(request):
    tasks = Tasks.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})


def task_create(request):
    form = TasksForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('task_list')
    return render(request, 'task_form.html', {'form': form})


def task_update(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    form = TasksForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('task_list')
    return render(request, 'task_form.html', {'form': form})


def task_delete(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    task.delete()
    return redirect('task_list')


def task_view(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    return render(request, 'task_view.html', {'task': task})
