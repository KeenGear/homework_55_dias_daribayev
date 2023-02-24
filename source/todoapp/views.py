from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Tasks


class TaskListView(ListView):
    model = Tasks
    template_name = 'task_list.html'
    context_object_name = 'tasks'
    ordering = ['-created_at']


class TaskDetailView(DetailView):
    model = Tasks
    template_name = 'task_view.html'
    context_object_name = 'task'


class TaskCreateView(CreateView):
    model = Tasks
    template_name = 'task_form.html'
    fields = ['title', 'text', 'img', 'description', 'author', 'status']
    success_url = reverse_lazy('tasks')


class TaskUpdateView(UpdateView):
    model = Tasks
    template_name = 'task_form.html'
    fields = ['title', 'text', 'img', 'description', 'author', 'status']
    success_url = reverse_lazy('tasks')


class TaskDeleteView(DeleteView):
    model = Tasks
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('tasks')
