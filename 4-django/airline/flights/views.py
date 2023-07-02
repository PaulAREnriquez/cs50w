from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Flight, Passenger


# Create your views here.
def index(request):
    context_dict = {"flights": Flight.objects.all()}
    return render(request, "flights/index.html", context=context_dict)


def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    context_dict = {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all(),
    }
    return render(request, "flights/flight.html", context=context_dict)


def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        # the data about which passenger id we want to register on this flight
        # is going to be passed in via a form which input field has a name called "passenger"
        # we need to convert it into an integer because it is string by default

        # TODO: error checking might include the existence of the passenger
        # TODO: and the existence of the flight
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        # adding a flight to a set called flights
        passenger.flights.add(flight)

        # args=(flight.id,) must be structured as a tuple
        return HttpResponseRedirect(reverse("flights:flight", args=(flight.id,)))
