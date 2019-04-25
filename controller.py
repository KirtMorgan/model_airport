from person import Person
from passenger import Passenger
from flight import *
from plane import Plane

user_input = 0
while True:
    print('Gatwick airport terminal V0.1, please select a option below')
    print('\n 1)Create a passenger''\n 2)Show list of flights''\n 3)Add passenger to existing flight')
    user_input = int(input('Your selection = '))

    if user_input == 1:
        print('Create a passenger')
        name = input('Please enter the passengers name')
        passport_number = input('Please enter the passengers passport number')
        gender = input('Please enter the gender of the passenger')
        nationality = input('Please enter the passengers nationality')
        new_passenger = Passenger(name, passport_number, gender, nationality)
        print('\n This is the information for the new passenger', new_passenger.name, new_passenger.passport_number, new_passenger.gender, new_passenger.nationality)

    elif user_input == 2:
        print('List of current flights')
        for flights in list_flights:
            print(flights.origin_destination)

    elif user_input == 3:
        print('Add passenger to existing flight')
        user_input = int(input('Please select a flight (1, 2, 3, 4, 5'))
        if user_input == 1:
            print('Passenger', flight_01.add_passenger(new_passenger),' Has been added to flight', list_flights[0].origin_destination)

            print(flight_01)
        elif user_input == 2:
            print(list_flights[1].origin_destination)
        elif user_input == 3:
            print(list_flights[2].origin_destination)
        elif user_input == 4:
            print(list_flights[3].origin_destination)
        elif user_input == 5:
            print(list_flights[4].origin_destination)



#I want to add a passanger to existing flights

        # We should list all existing flights (see above)
        # select a flight
            # prom user for input and use some kind of index to select a flight
            # access flight from list using the index
        # create a new passanger objct (see above)

        # run the .add_passanger method on said flight and
            # pass in the passanger object(it's a variable)


    else:
        print('Invalid input, please enter a valid input')

