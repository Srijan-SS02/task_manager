from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse

tasks= []   #creating empty list to store task
# Create your views here.


class NewtaskForm(forms.Form):
    task=forms.CharField(label="Add_Task")



def index(request):
    return render(request, "mytask/index.html", {
        "tasks":tasks
    })


def add(request):
    if request.method == 'POST':
        form = NewtaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
            return HttpResponseRedirect(reverse())
    return render(request, "mytask/add.html", {
        "form": NewtaskForm()
    })    

