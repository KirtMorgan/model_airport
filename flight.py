from passenger import *
from plane import *

class Flight:
    def __init__(self, origin_destination='', plane=''):
        self.origin_destination = origin_destination
        self.plane = plane
        self.passengers_list = []

    def add_plane(self, plane):
        self.plane = plane

    def add_origin_destination(self, origin_destination):
        self.origin_destination = origin_destination

    def add_passenger(self, passenger):
        self.passengers_list.append(passenger)

# Airlines
airline_1 = Flight('UK - New Vegas', Boeing_747_8.owner)
airline_2 = Flight('Turkey - Paris', Boeing_747_400.owner)
airline_3 = Flight('New York - UK', Boeing_747_400ER.owner)
airline_4 = Flight('Spain - Portugal', Boeing_777_300.owner)
airline_5 = Flight('France - Germany', Boeing_777_300ER.owner)

list_flights = []
list_flights.append(airline_1)
list_flights.append(airline_2)
list_flights.append(airline_3)
list_flights.append(airline_4)
list_flights.append(airline_5)

list_passengers = []
list_passengers.append(passenger_1)
list_passengers.append(passenger_2)
list_passengers.append(passenger_3)
list_passengers.append(passenger_4)
list_passengers.append(passenger_5)