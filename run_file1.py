# from plane_class import *
# from people_class import *
# from flight_trip_class import *
from pip._vendor.distlib.compat import raw_input

import passenger_class
from login import *
from main_menu import *
from passenger_class import *

# from aircraft_class import *

class run_airport:
    # # Initialise lists
    plane_list = []
    flight_list = []

    log.check()

    loop = True

    while loop:  # While loop which will keep going until loop = False
        print_menu()  # Displays menu
        choice = int(input("Enter your choice [1-5]: "))

        if choice == 1:
            print('Create a Passenger has been selected')
            print(passenger_class.passenger.create_passenger())
        if choice == 2:
            print('Create a Passenger has been selected')
        if choice == 3:
            print('Create a Passenger has been selected')
        if choice == 4:
            print('Create a Passenger has been selected')
        if choice == 5:
            print('Shutting Down Now....')
            loop = False
        else:
            raw_input("Wrong option selection. Enter any key to try again..")

    # I can create 'Joana Thomson' with the Passport number 'B343123'
    # I can create 'Birt Kuman' with the Passport number 'B13927'


