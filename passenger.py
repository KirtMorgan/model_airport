from person import Person

class Passenger(Person):
    def __init__(self, name, passport_number, gender, nationality):
        super().__init__(name, gender, nationality)
        self.passport_number = passport_number


passenger_1 = Passenger('Bob Hill', 'AM135060', 'Male', 'British')
passenger_2 = Passenger('Liam Fort', 'AM135160', 'Male', 'French')
passenger_3 = Passenger('Catherine Winehouse', 'AM1375460', 'Female', 'Dutch')
passenger_4 = Passenger('Daisy Bloom', 'AM253732', 'Female', 'British')
passenger_5 = Passenger('Carl Bigland', 'AM646393', 'Male', 'Turkish')
