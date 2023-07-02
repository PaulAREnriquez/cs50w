from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
    """
    Display an information about a currently signed in user
    """

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
    
    return render(request, 'users/user.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        # authenticate checks if the username and password are correct
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('users:index'))
        else:
            context_dict = {"message": "Invalid username or password."}

            return render(request, 'users/login.html', context=context_dict)

def logout_view(request):
    logout(request)
    context_dict = {"message": "Logout successful."}
    return render(request, 'users/login.html', context=context_dict)
