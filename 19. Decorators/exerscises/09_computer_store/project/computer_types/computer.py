from abc import ABC, abstractmethod
from math import log2

class Computer(ABC):
    def __init__(self, manufacturer: str, model: str):
        self.__manufacturer = manufacturer
        self.__model = model
        self.processor: str | None = None
        self.ram: int | None = None
        self.price: int = 0

    @property
    @abstractmethod
    def valid_processor(self) -> dict[str, int]:
        pass

    @property
    @abstractmethod
    def max_ram(self) -> int:
        pass

    @property
    def valid_ram(self) -> list[int]:
        return [2 ** i for i in range(1, int(log2(self.max_ram) + 1))]

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if value.strip() == '':
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.strip() == '':
            raise ValueError("Model name cannot be empty.")
        self.__model = value

    @abstractmethod
    def __str__(self):
        pass

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.valid_processor:
            raise ValueError(f"{self.processor} is not compatible with {self.__str__()} {self.__manufacturer} {self.__model}!")
        if ram not in self.valid_ram:
            raise ValueError(f"{self.ram}GB RAM is not compatible with {self.__str__()} {self.__manufacturer} {self.__model}!")

        self.processor = processor
        self.ram = ram
        ram_price = int(log2(ram) * 100)
        self.price = self.valid_processor[processor] + ram_price

        return f"Created {self.__manufacturer} {self.__model} with {self.processor} and {self.ram}GB RAM for {self.price}$."

    def __repr__(self):
        return f"{self.__manufacturer} {self.__model} with {self.processor} and {self.ram}GB RAM"