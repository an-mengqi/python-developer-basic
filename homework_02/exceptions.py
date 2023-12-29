"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class BaseVehicleException(Exception):
    pass


class LowFuelError(BaseVehicleException):
    def __init__(self, message):
        super().__init__("Low fuel!" + " " + message)


class NotEnoughFuel(BaseVehicleException):
    def __init__(self, message):
        super().__init__("Not enough fuel!" + " " + message)


class CargoOverload(BaseVehicleException):
    def __init__(self, message):
        super().__init__("Not overload!" + " " + message)
