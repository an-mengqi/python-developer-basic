"""
создайте класс `Plane`, наследник `Vehicle`
"""
import exceptions

from base import Vehicle


class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, load_amount):
        if load_amount + self.cargo <= self.max_cargo:
            self.cargo += load_amount
            return load_amount
        else:
            raise exceptions.CargoOverload(f"Maximum is {self.max_cargo} kg, you loaded {self.cargo + load_amount} kg")

    def remove_all_cargo(self):
        loaded_amount = self.cargo
        self.cargo = 0
        return loaded_amount
