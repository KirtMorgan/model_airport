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
flight_01 = Flight('UK - New Vegas')
flight_02 = Flight('Turkey - Paris')
flight_03 = Flight('New York - UK')
flight_04 = Flight('Spain - Portugal')
flight_05 = Flight('France - Germany')

#list of flights

# flight_01 = Flight()
# flight_01.add_plane(Boeing_747_8)
# flight_01.add_origin_destination(flight_01)
# flight_01.add_passenger(passenger_1)

list_flights = []
list_flights.append(flight_01)
list_flights.append(flight_02)
list_flights.append(flight_03)
list_flights.append(flight_04)
list_flights.append(flight_05)



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














