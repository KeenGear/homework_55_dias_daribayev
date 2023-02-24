from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Tasks
from .forms import TasksForm


class TaskListView(ListView):
    model = Tasks
    context_object_name = 'tasks'
    template_name = 'task_list.html'


class TaskDetailView(DetailView):
    model = Tasks
    context_object_name = 'task'
    template_name = 'task_view.html'


class TaskCreateView(CreateView):
    model = Tasks
    form_class = TasksForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')


class TaskUpdateView(UpdateView):
    model = Tasks
    form_class = TasksForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')


class TaskDeleteView(DeleteView):
    model = Tasks
    context_object_name = 'task'
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('task_list')
