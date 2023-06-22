from django.db import models


# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f"{self.city} ({self.code})"


class Flight(models.Model):
    # origin = models.CharField(max_length=64)
    # destination = models.CharField(max_length=64)

    # on_delete=models.CASCADE means when the data that you are referencing from another table gets deleted
    # related_name is used to access a relationship in a reverse order
    # For example, you can access origin trough a flight using flight.origin
    # In the same way, you can know if you have an airport, you can know if a flight has that airport as its origin
    
    origin = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="departures"
    )
    # related_name="arrivals" gives you a way to know if you have an airport
    # what are the flights that has that airport as their destination
    destination = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="arrivals"
    )
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

class Passenger(models.Model):
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    # Every passenger has flights associated with them
    # blank=True means passenger can have no flights
    # related_name='passengers' means passenger.flights gets you all the flights for that passenger
    # flight.passengers lets you access all the passengers for that flight
    flights = models.ManyToManyField(Flight,blank=True,related_name="passengers")

    def __str__(self):
        return f"{self.firstname} {self.lastname}"