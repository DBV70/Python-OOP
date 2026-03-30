from abc import ABC, abstractmethod
from project.products.base_product import BaseProduct

class BaseStore(ABC):
    def __init__(self, name: str, location: str, capacity: int):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.products: list[BaseProduct] = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Store name cannot be empty!")
        self._name = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        if value.strip() == '' or len(value) != 3:
            raise ValueError("Store location must be 3 chars long!")
        self._location = value

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Store capacity must be a positive number or 0!")
        self._capacity = value

    def get_estimated_profit(self):
        profit = sum(p.price for p in self.products) * 0.1
        return f"Estimated future profit for {len(self.products)} products is {profit:.2f}"

    @property
    @abstractmethod
    def store_type(self) -> str:
        pass

    @property
    @abstractmethod
    def _product_section_text(self):
        pass

    def store_stats(self):
        products = {}
        for product in self.products:
            if product.model not in products:
                products[product.model] = {"qty": 0, "total_price": 0.0}
            products[product.model]["qty"] += 1
            products[product.model]["total_price"] += product.price

        result = [
            f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}",
            self.get_estimated_profit(),
            self._product_section_text,
            ]

        for model in sorted(products.keys()):
            qty = products[model]["qty"]
            average_price = products[model]["total_price"] / qty
            result.append(f"{model}: {qty}pcs, average price: {average_price:.2f}")

        return '\n'.join(result).strip()
