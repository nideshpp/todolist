from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import TodoListItem

# Create your views here.
def todoappview(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request,'todolist.html',{'all_items':all_todo_items})

def addTodoview(request):
    x= request.POST['content']
    new_item = TodoListItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/todoapp')