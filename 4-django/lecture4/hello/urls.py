from django.urls import path
from . import views

# The empty string "" is the default route
urlpatterns = [
    path("", views.index, name="index"),
    path("paul", views.paul, name="paul"),
    path("<str:name>", views.greet, name="greet"),
]
