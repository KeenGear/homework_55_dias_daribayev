from django.urls import path
from .views import task_list, task_create, task_delete, task_update, task_view

urlpatterns = [
    path('', task_list, name='task_list'),
    path('create/', task_create, name='task_create'),
    path('update/<int:pk>/', task_update, name='task_update'),
    path('delete/<int:pk>/', task_delete, name='task_delete'),
    path('task/<int:pk>/', task_view, name='task_view'),
]
