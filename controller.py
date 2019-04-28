from person import Person
from passenger import Passenger
from flight import *
from plane import Plane
terminal_input = 0
while True:
    print('Gatwick airport terminal V0.1, please select a option below')
    print(' 1)Create a passenger''\n 2)Show list of flights''\n 3)Add passenger to existing flight''\n 4)List passengers for a selected flight')
    terminal_input = int(input('Your selection = '))

    if terminal_input == 1:
        print('Create a passenger')
        name = input('Please enter the passengers name')
        passport_number = input('Please enter the passengers passport number')
        gender = input('Please enter the gender of the passenger')
        nationality = input('Please enter the passengers nationality\n')
        new_passenger = Passenger(name, passport_number, gender, nationality)
        list_passengers.append(new_passenger)
        for new in list_passengers:
            print(new.name, new.passport_number, new.gender, new.nationality)
        print('This is the information for the new passenger', new_passenger.name, new_passenger.passport_number, new_passenger.gender, new_passenger.nationality)

    elif terminal_input == 2:
        print('List of current flights')
        for flights in list_flights:
            print(flights.origin_destination)

    elif terminal_input == 3:
        print('Add passenger to existing flight')
        print('Please select a flight \n 1 - UK - New Vegas \n 2 - Turkey - Paris \n 3 - New York - UK \n 4 - Spain - Portugal \n 5 - France - Germany')
        user_input = int(input('Please make a selection'))

        if user_input == 1:
            print('You have selected flight UK - New Vegas')
            last_passenger = list_passengers[-1]
            flight_01.add_passenger(last_passenger)
            print('You have added', last_passenger.name, 'to flight', origin_destination01.origin_destination)

        elif user_input == 2:
            print('You have selected flight Turkey - Paris')
            last_passenger = list_passengers[-1]
            flight_02.add_passenger(last_passenger)
            print('You have added', last_passenger.name, 'to flight', origin_destination02.origin_destination)

        elif user_input == 3:
            print('You have selected flight New York - UK')
            last_passenger = list_passengers[-1]
            flight_03.add_passenger(last_passenger)
            print('You have added', last_passenger.name, 'to flight', origin_destination03.origin_destination)

        elif user_input == 4:
            print('You have selected flight Spain - Portugal')
            last_passenger = list_passengers[-1]
            flight_04.add_passenger(last_passenger)
            print('You have added', last_passenger.name, 'to flight', origin_destination04.origin_destination)

        elif user_input == 5:
            print('You have selected flight France - Germany')
            last_passenger = list_passengers[-1]
            flight_05.add_passenger(last_passenger)
            print('You have added', last_passenger.name, 'to flight', origin_destination05.origin_destination)

    elif terminal_input == 4:
        print( 'Please select a flight to view passengers \n 1 - UK - New Vegas \n 2 - Turkey - Paris \n 3 - New York - UK \n 4 - Spain - Portugal \n 5 - France - Germany')
        user_input = int(input('Please make a selection'))
        if user_input == 1:
            print('Please see below list for flight', origin_destination01.origin_destination)
            for flight_list in flight_01.passengers_list:
                print(flight_list.name)
        elif user_input == 2:
            print('Please see below list for flight', origin_destination02.origin_destination)
            for flight_list in flight_02.passengers_list:
                print(flight_list.name)
        elif user_input == 3:
            print('Please see below list for flight', origin_destination03.origin_destination)
            for flight_list in flight_03.passengers_list:
                print(flight_list.name)
        elif user_input == 4:
            print('Please see below list for flight', origin_destination04.origin_destination)
            for flight_list in flight_04.passengers_list:
                print(flight_list.name)
        elif user_input == 5:
            print('Please see below list for flight', origin_destination05.origin_destination)
            for flight_list in flight_05.passengers_list:
                print(flight_list.name)
    else:
         print('Invalid input, please enter a valid input')

