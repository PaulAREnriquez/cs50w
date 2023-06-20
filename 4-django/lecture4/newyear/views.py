from django.shortcuts import render
import datetime
# Create your views here.

def index(request):
    now = datetime.datetime.now()
    context_dict = {
        # if newyear is True
        "newyear": now.month == 1 and now.day==1
    }
    return render(request,"newyear/index.html", context=context_dict)
