from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

# this variable is a global variable that the entire application has access to
# this means that if we use this, anyone who visits our website will have the same tasks
# but we want to individualize the tasks for each user
# so we have to do it another way
# tasks = []


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    # the constraints defined for this IntegerField
    # are just client-side validation
    # it means that the web page has been encoded to know what the valid values are

    # we also want to make sure not only client-side validation but also
    # server-side validation
    # it is easy to disable client-side validation, and also validation may be out of date
    # and do not match the requirements
    # sometimes either one of client and server-side validation are outdated
    # the server-side validation will still be able to prevent invalid inputs to forms

    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)


# Create your views here.
def index(request):
    

    # this is where we use sessions in Django instead of a global variable
    # sessions remember a user's session individually
    # it stores a session per user in a table called django_session
    # in order to create that table,
    # we need to run in the terminal `python manage.py migrate`
    # it allows us to create all the default tables in Django database

    # everytime a user access a page
    # they will see a different version that is unique to them 
    if "tasks" not in request.session:
        request.session["tasks"] = []

    # context_dict = {"tasks":tasks}
    context_dict = {"tasks": request.session["tasks"]}
    return render(request, "tasks/index.html", context=context_dict)


def add(request):
    if request.method == "POST":
        # request.POST contains all the data the user submitted
        # and we will pass it as an argument to NewTaskForm
        form = NewTaskForm(request.POST)
        context_dict = {"form": form}

        # this is the server-side validation
        if form.is_valid():
            task = form.cleaned_data["task"]

            # tasks.append(task)
            request.session["tasks"] += [task]

            # redirects the user to a particular route
            # we give the name of the route we want to redirect the user
            # and pass it as an argument to reverse()
            # this means Django will reverse engineer and find what that route is for us
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            # we send back the populated form by the user
            # so we can display information and  they can know what went wrong
            return render(request, "tasks/add.html", context=context_dict)

    # if the user just goes to the page without submitting a form
    return render(request, "tasks/add.html", context={"form": NewTaskForm()})
