from todo.models import Todo
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def top(request):
    todos = Todo.objects.all()
    context = {
      'todos': todos
    }
    return render(request, 'todo/top.html', context)