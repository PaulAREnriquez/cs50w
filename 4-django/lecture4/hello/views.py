from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    """
    request represents the HTTP request made to access the web server.
    request contains metadata on what the HTTP request is about.

    """
    return render(request, "hello/index.html")


def paul(request):
    return HttpResponse("Hello, Paul!")


def greet(request, name):
    context_dict = {
        "name": name.capitalize(),
    }
    # context_dict is the context in which our template to render has access to
    return render(request, "hello/greet.html", context=context_dict)
