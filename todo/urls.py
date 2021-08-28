from todo import views
from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('new/',views.todo_new, name='new'),
    path('<int:todo_id>/delete/',views.todo_delete, name='delete'),
    path('<int:todo_id>/detail/',views.todo_detail, name='detail'),
    path('<int:todo_id>/edit/',views.todo_edit, name='edit'),
]
