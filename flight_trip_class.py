class FlightTrip:
    def __init__(self, origin, destination, plane_number, flight_id, list_of_passenger=[]):
        self.origin = origin
        self.destination = destination
        self.list_of_passenger = list_of_passenger
        self.plane_number = plane_number
        self.flight_id = flight_id


# use getters and setters

# As a user I can create a flight with no specific information
# as a user I can add a plane
# as a User I can add a destination
# As a user I can add a origin
# As a user I can add a Passenger to the list of passengers
# Passenger list is a list of object that are Passenger

    def create_flight_trip(self):
        while True:
            question = input('Would you like to create a flight trip? y/n')
            if question == 'y':
                question = input('Would you like to add details? y/n')
                if question == 'y':
                    origin = input('Please enter the origin of the flight.')
                    destination = input('Please enter the destination of the flight.')
                    list_of_passengers = input('Please enter the list of passengers.')
                    plane_number = input('Please input the plane number of the flight.')
                    flight_id = len(flight_list)
                    flight_trip = FlightTrip(origin, destination, list_of_passengers, plane_number, flight_id)
                elif question == 'n':
                    flight_trip = FlightTrip()
            elif question == 'n':
                print('Thanks')
                break
