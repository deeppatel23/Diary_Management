from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import memory
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
User = get_user_model()


@login_required(login_url='/accounts/login')
def show(request):
    log_user = request.user
    memories = memory.objects.filter(user=log_user)
    return render(request, 'diary-home.html', {'m':memories})

@login_required(login_url='/accounts/login')
def add(request):
    title = request.POST['title']
    description = request.POST['description']
    new = memory(title=title, description=description, user=request.user)
    new.save()
    return redirect('show')
    

def delete(request, todo_id):
    todo = get_object_or_404(memory, pk=todo_id)
    todo.delete()
    return redirect('show')

def update(request, todo_id):
    todo = get_object_or_404(memory, pk=todo_id)
    title = request.POST['title']
    description = request.POST['description']
    todo.title = title
    todo.description = description
    todo.save()
    return redirect('show')

