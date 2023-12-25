from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView
from .models import Task


# Create your views here.
class HomeView(ListView):
    template_name = 'home.html'
    model = Task

    # task = Task.objects.filter(is_complete=False)
    # completed_tasks = Task.objects.filter(is_complete=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(is_complete=False).order_by('-updated_at')
        context['completed_tasks'] = Task.objects.filter(is_complete=True)
        return context

    def addTask(request):
        task = request.POST['task']
        Task.objects.create(task=task)
        return redirect('home')

    def mark_as_done(request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_complete = True
        task.save()
        return redirect('home')

    def mark_as_undone(request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_complete = False;
        task.save()
        return redirect('home')

    def edit_task(request, pk):
        task = get_object_or_404(Task, pk=pk)
        if request.method == 'POST':
            # Update the task with the new data from the form
            task.task = request.POST.get('task')
            task.save()
            return redirect('home')  # Redirect to the home page after editing
        else:
            context = {'task': task}
            return render(request, 'edit_task.html', context)

    def delete_task(request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('home')
