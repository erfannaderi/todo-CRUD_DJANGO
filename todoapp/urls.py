from django.urls import path
from .views import addTask

urlpatterns = [
    path('addTask/', addTask, name='addTask'),
]
