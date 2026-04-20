# Module for creating vehicles using the Factory Method pattern

import logging

from abc import ABC, abstractmethod
from typing import Type

logger = logging.getLogger("VehicleLogger")
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(message)s")
console_handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(console_handler)


class Vehicle(ABC):
    def __init__(self, make: str, model: str) -> None:
        self.make: str = make
        self.model: str = model

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model}: The car engine is started")


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model}: The motorcycle engine is started")


class VehicleFactory(ABC):
    @abstractmethod
    def get_region_spec(self) -> str:
        pass

    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, f"{model} ({self.get_region_spec()})")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, f"{model} ({self.get_region_spec()})")


class USVehicleFactory(VehicleFactory):
    def get_region_spec(self) -> str:
        return "US Spec"


class EUVehicleFactory(VehicleFactory):
    def get_region_spec(self) -> str:
        return "EU Spec"


if __name__ == "__main__":
    eu_factory: VehicleFactory = EUVehicleFactory()

    vehicle1: Vehicle = eu_factory.create_car("VW", "Beetle")
    vehicle1.start_engine()

    vehicle2: Vehicle = eu_factory.create_motorcycle("BMW", "R12")
    vehicle2.start_engine()

    us_factory: VehicleFactory = USVehicleFactory()

    vehicle3: Vehicle = us_factory.create_car("Ford", "Mustang")
    vehicle3.start_engine()

    vehicle4: Vehicle = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
    vehicle4.start_engine()
