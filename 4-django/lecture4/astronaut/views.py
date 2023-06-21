from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms


class AstronautForm(forms.Form):
    name = forms.CharField(label="Name of Applicant ")
    height = forms.IntegerField(label="Height in cm. ", min_value=100, max_value=300)


def result(request):
    if "applicant" not in request.session:
        request.session["applicant"] = {}

    context_dict = {"applicant": request.session["applicant"]}
    return render(request, "astronaut/result.html", context=context_dict)


def index(request):
    if request.method == "POST":
        form = AstronautForm(request.POST)
        context_dict = {"form": form}
        if form.is_valid():
            name = form.cleaned_data["name"]
            height = form.cleaned_data["height"]
            request.session["applicant"] = {"name": name, "height": height}
            return HttpResponseRedirect(reverse("astronaut:result"))
        else:
           return render(request, "astronaut/index.html", context=context_dict)

    return render(request, "astronaut/index.html", context={"form": AstronautForm()})
