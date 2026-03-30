from project.products.base_product import BaseProduct
from project.stores.base_store import BaseStore
from project.stores.toy_store import ToyStore
from project.stores.furniture_store import FurnitureStore
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse

class FactoryManager:
    def __init__(self, name: str):
        self.name = name
        self.income: float = 0.0
        self.stores: list[BaseStore] = []
        self.products: list[BaseProduct] = []

    def produce_item(self, product_type: str, model: str, price: float):
        product_class = {"Chair": Chair, "HobbyHorse": HobbyHorse}.get(product_type)
        if not product_class:
            raise Exception(f"Invalid product type!")
        new_product = product_class(model, price)
        self.products.append(new_product)
        return f"A product of sub-type {new_product.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        store_class = {"ToyStore": ToyStore, "FurnitureStore": FurnitureStore}.get(store_type)
        if not store_class:
            raise Exception(f"{store_type} is an invalid type of store!")
        new_store = store_class(name, location)
        self.stores.append(new_store)
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        if store.capacity < len(products):
            return f"Store {store.name} has no capacity for this purchase."

        filtered_products = [p for p in products if p.sub_type.lower() in store.store_type.lower()]

        if not filtered_products:
            return f"Products do not match in type. Nothing sold."

        for product in filtered_products:
            store.products.append(product)
            self.products.remove(product)
            store.capacity -= 1
            self.income += product.price

        return f"Store {store.name} successfully purchased {len(filtered_products)} items."

    def unregister_store(self, store_name: str):
        store = next((s for s in self.stores if s.name == store_name), None)
        if not store:
            raise Exception("No such store!")
        if store.products:
            return "The store is still having products in stock! Unregistering is inadvisable."
        self.stores.remove(store)
        return f"Successfully unregistered store {store.name}, location: {store.location}."

    def discount_products(self, product_model: str):
        discounted_products = [p for p in self.products if p.model == product_model]
        [p.discount() for p in discounted_products]
        return f"Discount applied to {len(discounted_products)} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        store = next((s for s in self.stores if s.name == store_name), None)
        if not store:
            return f"There is no store registered under this name!"
        return store.store_stats()

    def statistics(self):
        products = {}
        total_net_price = 0.0
        for product in self.products:
            products[product.model] = products.get(product.model, 0) + 1
            total_net_price += product.price

        result = [
            f"Factory: {self.name}",
            f"Income: {self.income:.2f}",
            f"***Products Statistics***",
            f"Unsold Products: {len(self.products)}. Total net price: {total_net_price:.2f}",
            ]

        for product in sorted(products.keys()):
            result.append(f"{product}: {products[product]}")

        result.append(f"***Partner Stores: {len(self.stores)}***")

        for store in sorted(self.stores, key=lambda s: s.name):
            result.append(f"{store.name}")

        return '\n'.join(result).strip()
