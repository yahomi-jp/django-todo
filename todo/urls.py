from todo import views
from django.urls import path
from . import views
urlpatterns = [
    path('new/',views.todo_new, name='new'),
    path('<int:todo_id>/delete/',views.todo_delete, name='delete'),
]
