import todo
from django.http.response import HttpResponseForbidden
from todo.models import Todo
from todo.form import TodoForm
from django.shortcuts import get_object_or_404, redirect, render
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

@login_required
def todo_delete(request, todo_id):
    if request.method == 'POST':
        todo = get_object_or_404(Todo, pk=todo_id)
        if todo.created_by.id == request.user.id:
            todo.delete()
    
    return redirect(top)

@login_required
def todo_detail(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if todo.created_by.id == request.user.id:
        form = TodoForm(instance=todo)
        context = {
            'todo': todo,
            'form': form,
        }
        return render(request, 'todo/detail.html', context)
    else:
        return HttpResponseForbidden('このTodoの閲覧は許可されていません')

@login_required
def todo_edit(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.created_by = request.user
            todo.save()
            return redirect(top)
    else:
        return HttpResponseForbidden('正規の手続きを踏んでください')
