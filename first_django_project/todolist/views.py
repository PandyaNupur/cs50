from django.urls import reverse
from django.http import HttpResponseRedirect
from django import forms
from django.shortcuts import render
# tasks=[]
class NewTaskForm(forms.Form):
    task=forms.CharField(label="New Task")
    priority=forms.IntegerField(label="Priority", min_value=1,max_value=5)
# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"]=[]
    return render(request,"todolist/index.html",{
        "tasks":request.session["tasks"]
    })
def addtask(request):
    if request.method=="POST":
        form=NewTaskForm(request.POST) #populates this form with all of the data user has entered
        if form.is_valid():
            task=form.cleaned_data["task"]
            request.session["tasks"]+=[task]
            return HttpResponseRedirect(reverse("todolist:index"))
        else:
            return render(request,"todolist/add.html",{
                "form":form
            })
        
    return render(request,"todolist/add.html",{
        "form":NewTaskForm
    })