from todo.models import Todo
from todo.form import TodoForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def top(request):
    form = TodoForm
    todos = Todo.objects.all()
    context = {
      'todos': todos,
      'form': form,
    }
    return render(request, 'todo/top.html', context)