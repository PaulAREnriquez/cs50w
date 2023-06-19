# OOP
class Point:
    def __init__(self, **kwargs):
        """automatically called everytime a Point() instance
        is created
        """
        self.x = kwargs["x"]  # the value is stored in the class property called x
        self.y = kwargs["y"]  # the value is stored in the class property called y


point = Point(x=0, y=1, z=2)
print(point.x, point.y)


class Flight:
    def __init__(self, **kwargs):
        self.capacity = kwargs["capacity"]
        self.passengers = []

    def add_passengers(self, *args):
        for i in range(len(args)):
            if not self.open_seats(): # pythonic way of saying != 0
                break
            else:
                self.passengers.append(args[i])

    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = Flight(capacity=2)
flight.add_passengers("Ann", "Mae", "Cora", "Sheena")
print(f"Flight capacity: {flight.capacity}")
print(f"Passengers in flight: {flight.passengers}")
