from django.http import response
from django.shortcuts import render

# Create your views here.

def top(request):
    render(response, 'todo/top.html')