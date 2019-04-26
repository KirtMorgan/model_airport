from person import Person
from passenger import Passenger
from flight import *
from plane import Plane
terminal_input = 0
while True:
    print('Gatwick airport terminal V0.1, please select a option below')
    print('\n 1)Create a passenger''\n 2)Show list of flights''\n 3)Add passenger to existing flight')
    terminal_input = int(input('Your selection = '))

    if terminal_input == 1:
        print('Create a passenger')
        name = input('Please enter the passengers name')
        passport_number = input('Please enter the passengers passport number')
        gender = input('Please enter the gender of the passenger')
        nationality = input('Please enter the passengers nationality')
        new_passenger = Passenger(name, passport_number, gender, nationality)
        print('\n This is the information for the new passenger', new_passenger.name, new_passenger.passport_number, new_passenger.gender, new_passenger.nationality)

    elif terminal_input == 2:
        print('List of current flights')
        for flights in list_flights:
            print(flights.origin_destination)

    elif terminal_input == 3:
        print('Add passenger to existing flight')
        print('Please select a flight \n 1 - UK - New Vegas \n 2 - Turkey - Paris \n 3 - New York - UK \n 4 - Spain - Portugal \n 5 - France - Germany')
        user_input = int(input('Please make a selection'))
        print('Please select a passenger you wish to add \n 1 - Bob Hill \n 2 - Liam Fort \n 3 - Catherine Winehouse \n 4 - Daisy Bloom \n 5 - Carl Bigland')
        passenger_select = int(input('Please make a selection'))
        if user_input == 1:
            if passenger_select == 1:
                flight_01.add_passenger(passenger_1)
                print('Passenger', list_passengers[0].name, ' Has been added to flight', list_flights[0].origin_destination)
                # print(flight_01.passengers_list)
            elif passenger_select == 2:
                flight_01.add_passenger(passenger_2)
                print('Passenger', list_passengers[1].name, ' Has been added to flight',list_flights[0].origin_destination)
            elif passenger_select == 3:
                flight_01.add_passenger(passenger_3)
                print('Passenger', list_passengers[2].name, ' Has been added to flight',list_flights[0].origin_destination)
            elif passenger_select == 4:
                flight_01.add_passenger(passenger_4)
                print('Passenger', list_passengers[3].name, ' Has been added to flight',list_flights[0].origin_destination)
            elif passenger_select == 5:
                flight_01.add_passenger(passenger_5)
                print('Passenger', list_passengers[4].name, ' Has been added to flight',list_flights[0].origin_destination)
        elif user_input == 2:
            if passenger_select == 1:
                flight_02.add_passenger(passenger_1)
                print('Passenger', list_passengers[0].name, ' Has been added to flight', list_flights[1].origin_destination)
                # print(flight_01.passengers_list)
            elif passenger_select == 2:
                flight_02.add_passenger(passenger_2)
                print('Passenger', list_passengers[1].name, ' Has been added to flight',list_flights[1].origin_destination)
            elif passenger_select == 3:
                flight_02.add_passenger(passenger_3)
                print('Passenger', list_passengers[2].name, ' Has been added to flight',list_flights[1].origin_destination)
            elif passenger_select == 4:
                flight_02.add_passenger(passenger_4)
                print('Passenger', list_passengers[3].name, ' Has been added to flight',list_flights[1].origin_destination)
            elif passenger_select == 5:
                flight_02.add_passenger(passenger_5)
                print('Passenger', list_passengers[4].name, ' Has been added to flight',list_flights[1].origin_destination)
        elif user_input == 3:
            if passenger_select == 1:
                flight_03.add_passenger(passenger_1)
                print('Passenger', list_passengers[0].name, ' Has been added to flight', list_flights[2].origin_destination)
                # print(flight_01.passengers_list)
            elif passenger_select == 2:
                flight_03.add_passenger(passenger_2)
                print('Passenger', list_passengers[1].name, ' Has been added to flight',list_flights[2].origin_destination)
            elif passenger_select == 3:
                flight_03.add_passenger(passenger_3)
                print('Passenger', list_passengers[2].name, ' Has been added to flight',list_flights[2].origin_destination)
            elif passenger_select == 4:
                flight_03.add_passenger(passenger_4)
                print('Passenger', list_passengers[3].name, ' Has been added to flight',list_flights[2].origin_destination)
            elif passenger_select == 5:
                flight_03.add_passenger(passenger_5)
                print('Passenger', list_passengers[4].name, ' Has been added to flight',list_flights[2].origin_destination)
        elif user_input == 4:
            if passenger_select == 1:
                flight_04.add_passenger(passenger_1)
                print('Passenger', list_passengers[0].name, ' Has been added to flight', list_flights[3].origin_destination)
                # print(flight_01.passengers_list)
            elif passenger_select == 2:
                flight_04.add_passenger(passenger_2)
                print('Passenger', list_passengers[1].name, ' Has been added to flight',list_flights[3].origin_destination)
            elif passenger_select == 3:
                flight_04.add_passenger(passenger_3)
                print('Passenger', list_passengers[2].name, ' Has been added to flight',list_flights[3].origin_destination)
            elif passenger_select == 4:
                flight_04.add_passenger(passenger_4)
                print('Passenger', list_passengers[3].name, ' Has been added to flight',list_flights[3].origin_destination)
            elif passenger_select == 5:
                flight_04.add_passenger(passenger_5)
                print('Passenger', list_passengers[4].name, ' Has been added to flight',list_flights[3].origin_destination)

        elif user_input == 5:
            if passenger_select == 1:
                flight_05.add_passenger(passenger_1)
                print('Passenger', list_passengers[0].name, ' Has been added to flight', list_flights[4].origin_destination)
                # print(flight_01.passengers_list)
            elif passenger_select == 2:
                flight_05.add_passenger(passenger_2)
                print('Passenger', list_passengers[1].name, ' Has been added to flight',list_flights[4].origin_destination)
            elif passenger_select == 3:
                flight_05.add_passenger(passenger_3)
                print('Passenger', list_passengers[2].name, ' Has been added to flight',list_flights[4].origin_destination)
            elif passenger_select == 4:
                flight_05.add_passenger(passenger_4)
                print('Passenger', list_passengers[3].name, ' Has been added to flight',list_flights[4].origin_destination)
            elif passenger_select == 5:
                flight_05.add_passenger(passenger_5)
                print('Passenger', list_passengers[4].name, ' Has been added to flight',list_flights[4].origin_destination)
    else:
         print('Invalid input, please enter a valid input')

