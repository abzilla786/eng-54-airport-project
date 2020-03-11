from aircraft_class import *


class Plane(Aircraft):
    def __init__(self, plane_number, cargo):
        super().__init__(cargo)
        self.plane_number = plane_number

# Create planes
    def create_plane(self):
        while True:
            plane_number = input('Please enter the plane_number or write \'exit\' to exit.\n')
            if 'exit' in plane_number:
                break
            else:
                cargo = input('Please enter the cargo size.\n')
                plane = Plane(plane_number, cargo)
                plane_list.append(plane)

        [print(i.plane_number, i.cargo) for i in plane_list]