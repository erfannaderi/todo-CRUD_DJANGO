from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from .models import Task


# Create your views here.
class HomeView(ListView):
    template_name = 'home.html'
    model = Task
    task = Task.objects.filter(is_complete=False).order_by('-updated_at')


def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     tasks = Task.objects.all()  # Retrieve tasks from the database
    #     context['tasks'] = tasks  # Add tasks to the context
    #     return context
