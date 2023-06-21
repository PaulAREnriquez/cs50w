from django.urls import path
from . import views

app_name = 'astronaut'
# The empty string "" is the default route
urlpatterns = [
    path("", views.index, name="index"),
    path("result", views.result, name="result"),
]
