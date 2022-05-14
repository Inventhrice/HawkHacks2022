from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoListItem
# Create your views here.

def todo_app_view(request):
    all_todo_list_items = TodoListItem.objects.all()
    return render(request, 'index.html', {'all_items': all_todo_list_items})

def addTodo(request):
    msg = request.POST['content']
    new_item = TodoListItem(content = msg)
    new_item.save()
    return HttpResponseRedirect('/todo_app/')

def deleteTodo(request, i):
    item = TodoListItem.objects.get(id = i)
    item.delete()
    return HttpResponseRedirect('/todo_app/')