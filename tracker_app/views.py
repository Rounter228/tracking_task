from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .forms import TaskForm


class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "tracker_app/task_list.html"


class TaskDetailView(DetailView):
    model = Task
    context_object_name = "task"
    template_name = "tracker_app/task_detail.html"


class TaskCreateView(CreateView):
    model = Task
    template_name = "tracker_app/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("tracker_app:task_list")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tracker_app/task_confirm_delete.html"
    success_url = reverse_lazy("tracker_app:task_list")