from people_class import *


class Passenger(People):
    def __init__(self, name, passport_number):
        super().__init__(name)
        self.passport_number = passport_number

    # Create Passengers
    def create_passenger(self):
        while True:
            name = input('Please enter the plane_number or write \'exit\' to exit.\n')
            if 'exit' in plane_number:
                break
            else:
                passenger_number = input('Please enter the cargo size.\n')
                passenger = Passenger(name, passenger_number)
                passenger_list.append(passenger)

        [print(i.name, i.passenger_number) for i in passenger_list]