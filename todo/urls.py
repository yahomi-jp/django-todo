from todo import views
from django.urls import path
from . import views
urlpatterns = [
    path('new/',views.todo_new, name='new'),
]
