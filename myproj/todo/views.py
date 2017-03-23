from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Todo
from .forms import TaskForm


def index(request):
    template = loader.get_template('todo/index.html')
    return HttpResponse(template.render())


def see_tasks(request):
    todo_list = Todo.objects.all()
    template = loader.get_template('todo/see_tasks.html')
    context = {'todo_list': todo_list, }
    return HttpResponse(template.render(context, request))


def create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('')
    else:
        form = TaskForm()
    template = loader.get_template('todo/create.html')
    return HttpResponse(template.render())
    # return template.render({'form': form})
