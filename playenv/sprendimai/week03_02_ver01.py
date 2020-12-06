import csv
import os

class CarBase:   

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    car_type = "car"

    def __init__(self, brand, photo_file_name, 
                 carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        

    def set_passenger_seats_count(self, count):
        self.passenger_seats_count = count


class Truck(CarBase):
    car_type = "truck"
    
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl

        try:
            width, height, length = (float(c) for c in self.body_whl.split('x', 2))
        except ValueError:
            width, height, length = .0, .0, .0

        self.body_width = width
        self.body_height = height
        self.body_length = length

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length

class SpecMachine(CarBase):
    car_type = "spec_machine"

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra

#####TESTAVIMAS

car = Car('Bugatti Veyron', 'bugatti.png', '0.312', '2')
print(car.car_type, car.brand, car.photo_file_name, car.carrying, car.passenger_seats_count, sep='\n')
print()
spec_machine = SpecMachine('Komatsu-D355', 'd355.jpg', '93', 'pipelayer specs')
print(spec_machine.car_type, spec_machine.brand, spec_machine.carrying, spec_machine.photo_file_name, spec_machine.extra, sep='\n')
print()
truck = Truck('Nissan', 'nissan.jpeg', '1.5', '3.92x2.09x1.87')
print(truck.car_type, truck.brand, truck.photo_file_name, truck.body_length,truck.body_width, truck.body_height, sep='\n')
print()
######
base =CarBase('Bugatti Veyron', 'bugatti.png', '0.312')
print(base.get_photo_file_ext())
car =Car('Bugatti Veyron', 'bugatti.jpg', '0.312', '2')
print(car.get_photo_file_ext())
print(car.set_passenger_seats_count(5))
truck = Truck('Nissan', 'nissan.jpeg', '1.5', '3.92x2.09x1.87')
print(truck.get_body_volume())