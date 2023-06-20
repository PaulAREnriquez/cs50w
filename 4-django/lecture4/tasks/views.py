from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)


# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    context_dict = {"tasks": request.session["tasks"]}
    return render(request, "tasks/index.html", context=context_dict)


def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        context_dict = {"form": form}
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", context=context_dict)

    return render(request, "tasks/add.html", context={"form": NewTaskForm()})
