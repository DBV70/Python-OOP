from project.clients.business_client import BusinessClient
from project.clients.regular_client import RegularClient
from project.plants.base_plant import BasePlant
from project.clients.base_client import BaseClient
from project.plants.leaf_plant import LeafPlant
from project.plants.flower import Flower


class FlowerShopManager:
    VALID_PLANT_TYPES = {"Flower": Flower, "LeafPlant": LeafPlant}
    VALID_CLIENT_TYPES = {"RegularClient": RegularClient, "BusinessClient": BusinessClient}

    def __init__(self):
        self.income: float = 0.0
        self.plants: list[BasePlant] = []
        self.clients: list[BaseClient] = []

    def add_plant(self,
                  plant_type: str,
                  plant_name: str,
                  plant_price: float,
                  plant_water_needed: int,
                  plant_extra_data: str):

        if plant_type not in self.VALID_PLANT_TYPES.keys():
            raise ValueError(f"Unknown plant type!")

        plant = self.VALID_PLANT_TYPES[plant_type](
            plant_name,
            plant_price,
            plant_water_needed,
            plant_extra_data
            )
        self.plants.append(plant)
        return f"{plant_name} is added to the shop as {plant_type}."


    def add_client(self, client_type: str, client_name: str, client_phone_number: str):
        if client_type not in self.VALID_CLIENT_TYPES.keys():
            raise ValueError(f"Unknown client type!")

        if self._find_obj_by_phone_number(client_phone_number, self.clients) is not None:
            raise ValueError(f"This phone number has been used!")

        self.clients.append(self.VALID_CLIENT_TYPES[client_type](client_name, client_phone_number))
        return f"{client_name} is successfully added as a {client_type}."

    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int):
        client = self._find_obj_by_phone_number(client_phone_number, self.clients)
        if client is None:
            raise ValueError(f"Client not found!")

        plants_available = self._find_objs_by_name(plant_name, self.plants)
        if not plants_available:
            raise ValueError(f"Plant not found!")

        if plant_quantity > len(plants_available):
            return "Not enough plant quantity."

        total_price = sum(plant.price for plant in plants_available[:plant_quantity])
        discount = client.discount / 100
        order_amount = total_price * (1 - discount)
        self.income += order_amount

        for _ in range(plant_quantity):
            self.plants.remove(plants_available.pop(0))

        client.update_total_orders()
        client.update_discount()

        return f"{plant_quantity}pcs. of {plant_name} plant sold for {order_amount:.2f}"


    def remove_plant(self, plant_name: str):
        plants = self._find_objs_by_name(plant_name, self.plants)

        if not plants:
            return "No such plant name."

        plant_info = plants[0].plan_details()
        self.plants.remove(plants[0])
        return f"Removed {plant_info}"

    def remove_clients(self):
        initial_count = len(self.clients)
        self.clients = [c for c in self.clients if c.total_orders > 0]
        return f"{initial_count - len(self.clients)} client/s removed."

    def shop_report(self):
        total_orders = sum(c.total_orders for c in self.clients)
        result = ["~Flower Shop Report~",
                  f"Income: {self.income:.2f}",
                  f"Count of orders: {total_orders}",
                  f"~~Unsold plants: {len(self.plants)}~~"]

        unsold_plants = {}
        for plant in self.plants:
            unsold_plants[plant.name] = unsold_plants.get(plant.name, 0) + 1

        sorted_plants = dict(sorted(unsold_plants.items(), key=lambda x: (-x[1], x[0])))
        result.extend(f"{plant_name}: {quantity}" for plant_name, quantity in sorted_plants.items())

        result.append(f"~~Clients number: {len(self.clients)}~~")
        sorted_clients = sorted(self.clients, key=lambda x: (-x.total_orders, x.phone_number))

        for client in sorted_clients:
            result.append(client.client_details())
        return '\n'.join(result)

    # helper methods
    @staticmethod
    def _find_obj_by_phone_number(obj_phone_number, collection):
        return next((obj for obj in collection if obj.phone_number == obj_phone_number), None)

    @staticmethod
    def _find_objs_by_name(obj_name, collection):
        return [obj for obj in collection if obj.name == obj_name] or None