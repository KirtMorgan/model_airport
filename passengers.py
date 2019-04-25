from people import People
class Passengers(People):
    def __init__(self):
        super().__init__()
        self.passport_number = 0
    def create_passenger(self,name):
        name = 'Susan'
        self.name = name
        self.passport_number = '123643'

creator = Passengers
creator.create_passenger()

