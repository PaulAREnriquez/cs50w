from django.urls import path
from . import views

# this is to avoid namespace collisions among apps 
# with the same name of html file
# define a variable called app_name
app_name = "tasks"

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
]
