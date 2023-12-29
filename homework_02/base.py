import exceptions

from abc import ABC


class Vehicle(ABC):
    def __init__(self, weight=7000, fuel=300, fuel_consumption=25):
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        print(self.started)
        if not self.started:
            if self.fuel <= 0:
                raise exceptions.LowFuelError(f"Amount of fuel: {self.fuel}")
            else:
                self.started = True
            print(self.started)

    def move(self, distance):
        necessary_fuel_amount = distance * self.fuel_consumption
        if (self.fuel - necessary_fuel_amount) >= 0:
            self.fuel = self.fuel - necessary_fuel_amount
        else:
            raise (exceptions.NotEnoughFuel
                   (f"You need {necessary_fuel_amount - self.fuel} more liters of fuel for the {distance} km distance."))
