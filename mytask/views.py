from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import Addform
from .models import Addtask

# Create your views here.



def index(request):
    tasks= Addtask.objects.all()
    return render(request, "mytask/index.html", {
        "tasks":tasks
    })


def add(request):
    form = Addform()

    if request.method == 'POST':
        form = Addform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/mytask')

    return render(request, "mytask/add.html", {
        "form": form
    })    



def update(request, pk):
    task = Addtask.objects.get(id=pk)
    form = Addform(instance=task)

    if request.method == 'POST':
        form = Addform(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/mytask')
            
            
    return render(request,"mytask/add.html",{
        'form':form
    })    



def delete(request, pk):

    task = Addtask.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/mytask')   

    return render(request, "mytask/delete.html",{
        'task':task
    })    