from passenger import *
from plane import *

class Flight:
    def __init__(self, origin_destination=''):
        self.origin_destination = origin_destination
        self.plane = ''
        self.passengers_list = []

    def add_plane(self, plane):
        self.plane = plane

    def add_origin_destination(self, origin_destination):
        self.origin_destination = origin_destination

    # def add_destination(self, destination):
    #     self.destination = destination

    def add_passenger(self, passenger):
        self.passengers_list.append(passenger)


# Origins - Destinations
origin_destination01 = Flight('UK - New Vegas')
origin_destination02 = Flight('Turkey - Paris')
origin_destination03 = Flight('New York - UK')
origin_destination04 = Flight('Spain - Portugal')
origin_destination05 = Flight('France - Germany')

#list of flights

flight_01 = Flight()
flight_02 = Flight()
flight_03 = Flight()
flight_04 = Flight()
flight_05 = Flight()

list_flights = []
list_flights.append(origin_destination01)
list_flights.append(origin_destination02)
list_flights.append(origin_destination03)
list_flights.append(origin_destination04)
list_flights.append(origin_destination05)

list_passengers = []
list_passengers.append(passenger_1)
list_passengers.append(passenger_2)
list_passengers.append(passenger_3)
list_passengers.append(passenger_4)
list_passengers.append(passenger_5)

# #Creating a flight
# test_flight = Flight()
# # Adding a plane
# test_flight.add_plane(Boeing_747)
# # Adding an origin
# test_flight.add_origin()
# # Adding a destination
# test_flight.add_destination()
#
# # Adding passenger 1 - as a string
# test_flight.add_passenger(passenger_1)
# test_flight.add_passenger(passenger_2)
# test_flight.add_passenger(passenger_3)
# print(test_flight.plane, ('Your flight origin is', test_flight.origin), ('Your destination is',test_flight.destination), test_flight.passengers_list)














