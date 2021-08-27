from django.http.response import HttpResponseForbidden
from todo.models import Todo
from todo.form import TodoForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def top(request):
    form = TodoForm
    todos = Todo.objects.all().order_by('-id')
    context = {
      'todos': todos,
      'form': form,
    }
    return render(request, 'todo/top.html', context)

@login_required
def todo_new(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.created_by = request.user
            todo.save()
            return redirect(top)
    else:
        return HttpResponseForbidden('正規の手続きを踏んでください')