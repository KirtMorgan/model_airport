from person import *
from passenger import *
from flight import *
from plane import *
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
            print('Flight', flights.origin_destination, 'With', flights.plane)

    elif terminal_input == 3:
        print('Add passenger to existing flight')
        print('Please select a flight \n 1 - UK - New Vegas \n 2 - Turkey - Paris \n 3 - New York - UK \n 4 - Spain - Portugal \n 5 - France - Germany')
        user_input = int(input('Please make a selection'))

        if user_input == 1:
            print('You have selected flight', airline_1.origin_destination)
            last_passenger = list_passengers[-1]
            airline_1.add_passenger(last_passenger)
            print('You have added', last_passenger.name, 'to flight', airline_1.origin_destination)

        elif user_input == 2:
            print('You have selected flight', airline_2.origin_destination)
            last_passenger = list_passengers[-1]
            airline_2.add_passenger(last_passenger)
            print('You have added', last_passenger.name, 'to flight', airline_2.origin_destination)

        elif user_input == 3:
            print('You have selected flight ', airline_3.origin_destination)
            last_passenger = list_passengers[-1]
            airline_3.add_passenger(last_passenger)
            print('You have added', last_passenger.name, 'to flight', airline_3.origin_destination)

        elif user_input == 4:
            print('You have selected flight', airline_4.origin_destination)
            last_passenger = list_passengers[-1]
            airline_4.add_passenger(last_passenger)
            print('You have added', last_passenger.name, 'to flight', airline_4.origin_destination)

        elif user_input == 5:
            print('You have selected flight', airline_5.origin_destination)
            last_passenger = list_passengers[-1]
            airline_5.add_passenger(last_passenger)
            print('You have added', last_passenger.name, 'to flight', airline_5.origin_destination)

    elif terminal_input == 4:
        print( 'Please select a flight to view passengers \n 1 - UK - New Vegas \n 2 - Turkey - Paris \n 3 - New York - UK \n 4 - Spain - Portugal \n 5 - France - Germany')
        user_input = int(input('Please make a selection'))
        if user_input == 1:
            print('Please see below passenger list for flight', airline_1.origin_destination)
            for flight_list in airline_1.passengers_list:
                print(flight_list.name)
        elif user_input == 2:
            print('Please see below passenger list for flight', airline_2.origin_destination)
            for flight_list in airline_2.passengers_list:
                print(flight_list.name)
        elif user_input == 3:
            print('Please see below passenger list for flight', airline_3.origin_destination)
            for flight_list in airline_3.passengers_list:
                print(flight_list.name)
        elif user_input == 4:
            print('Please see below passenger list for flight', airline_4.origin_destination)
            for flight_list in airline_4.passengers_list:
                print(flight_list.name)
        elif user_input == 5:
            print('Please see below passenger list for flight', airline_5.origin_destination)
            for flight_list in airline_5.passengers_list:
                print(flight_list.name)
    else:
         print('Invalid input, please enter a valid input')

