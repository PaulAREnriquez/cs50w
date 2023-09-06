from django.urls import path
from . import views

# The empty string "" is the default route
# name is a useful attribute when we want to reference
# that view in other parts of the application
urlpatterns = [
    path("", views.index, name="index"),
    path("paul", views.paul, name="paul"),
    path("<str:name>", views.greet, name="greet"),
]
