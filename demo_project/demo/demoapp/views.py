from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import Todo

# Create your views here.


def withoutapi(request):
    todos = Todo.objects.all()
    return render(request, 'withoutapi.html', {'todos': todos})

def withoutapidetail(request, pk):
    todo = Todo.objects.get(pk=pk)
    return render(request, 'withoutapidetail.html', {'todo': todo})

def withapi(request):
    todos = list(Todo.objects.all().values())
    print(todos)
    return JsonResponse({'todos': todos})

def withapidetail(request, pk):
    todo = Todo.objects.get(pk=pk)
    return JsonResponse(model_to_dict(todo))