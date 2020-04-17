from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.utils import timezone
from .models import Todo
from django.http import HttpResponseRedirect
@csrf_exempt
def index(request):
    """ getting all the data into one  in order by date"""
    todoData = Todo.objects.all().order_by("-date")
    """ sending data up to the html """
    return render(request, 'index.html',{
         "todo": todoData
         }
        )
@csrf_exempt
def submit(request):
     current_date = timezone.now()
     """Getting data form imput post"""
     content = request.POST["thing"]
     print(content)
     print(current_date)
     """Creating model type object and saving the value"""
     Todo.objects.create(date = current_date , text = content)
     return HttpResponseRedirect('/')
@csrf_exempt
def delete(request, todo_id):
    print(todo_id)
    Todo.objects.get(id = todo_id).delete()
    return HttpResponseRedirect('/')



