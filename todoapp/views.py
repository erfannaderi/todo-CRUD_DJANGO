from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Task

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'
    model = Task

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     tasks = Task.objects.all()  # Retrieve tasks from the database
    #     context['tasks'] = tasks  # Add tasks to the context
    #     return context
