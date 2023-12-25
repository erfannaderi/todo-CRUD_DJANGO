from django.urls import path
from todoapp.views import HomeView

urlpatterns = [
    #add tasks to the
    path('addTask/', HomeView.addTask, name='addTask'),
    #add tasks to the done
    path('mark_as_done/<int:pk>/',HomeView.mark_as_done, name='mark_as_done'),
    #mark tasks as undone
    path('mark_as_undone/<int:pk>/', HomeView.mark_as_undone, name='mark_as_undone'),
    #edit tasks
    path('edit_task/<int:pk>/', HomeView.edit_task, name='edit_task'),
    #delete tasks
    path('delete_task/<int:pk>/', HomeView.delete_task, name='delete_task'),
]
