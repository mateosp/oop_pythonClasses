from calendar import c
from typing_extensions import Self

class Car:
    def __init__(self, make, model, year):
        #class for car registration.
        self.make = make
        self.model = model
        self.year = year

        #fuel capacity.
        self.fuel_capacity = 15
        self.fuel_level = 0

    def fill_tank(self):
        #methof for filling tank
        self.fuel_level = self.fuel_capacity
        print ("The tank is full!")

    def drive(self):
        #drive simulation
        print ("You are driving!")

        my_car = Car("Renault", "Stepway", "2020")
        print(my_car.make)
        print(my_car.model)
        print(my_car.year)
        my_car.fill_tank() #calling methods for knowing the fill tank level
        my_car.drive() #calling methods for knowing if it is in drive mode

        my_oldCar = Car("Renault", "Logan", "2011")
        my_oldCar.fuel_capacity = 12

        my_futureCar = Car("Renault", "Captur", "2022")
        my_futureCar.fuel_level = 12

    def update_fuel_level(self, new_level):
        #method for updating fuel level
        if (new_level <= self.fuel_capacity):
            self.fuel_level = new_level
        else:
            print("The limit is 15")

    def adding_fuel(self, amount):
        #method for adding fuel to the tank
        if (self.fuel_level + amount <= self.fuel_capacity):
            self.fuel_level += amount
        else: 
            print ("ypu have exceeded the limit")

#son class
class electricCar(Car): 
    def __init__(self, make, model, year):
        super().__init__(make, model, year) #super() it is like a function to heredate attributes from the main class


    