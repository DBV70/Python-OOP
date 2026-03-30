from project.battleships.base_battleship import BaseBattleship
from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone
from project.zones.pirate_zone import PirateZone
from project.zones.royal_zone import RoyalZone


class BattleManager:
    def __init__(self):
        self.zones: list[BaseZone] = []
        self.ships: list[BaseBattleship] = []

    def add_zone(self, zone_type: str, zone_code: str):
        zone = {"RoyalZone": RoyalZone, "PirateZone": PirateZone}.get(zone_type)
        if not zone:
            raise Exception("Invalid zone type!")

        if zone in self.zones:
            raise Exception("Zone already exists!")

        self.zones.append(zone(zone_code))
        return f"A zone of type {zone_type} was successfully added."

    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int):
        ship = {"RoyalBattleship": RoyalBattleship, "PirateBattleship": PirateBattleship}.get(ship_type)
        if not ship:
            raise Exception(f"{ship_type} is an invalid type of ship!")

        self.ships.append(ship(name, health, hit_strength))
        return f"A new {ship_type} was successfully added."

    @staticmethod
    def add_ship_to_zone(zone: BaseZone, ship: BaseBattleship):
        if zone.volume <= 0:
            return f"Zone {zone.code} does not allow more participants!"
        if ship.health <= 0:
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"
        if not ship.is_available:
            return f"Ship {ship.name} is not available and could not participate!"
        if ship.ship_type == zone.zone_name:
            ship.is_attacking = True
        else:
            ship.is_attacking = False

        zone.ships.append(ship)
        ship.is_available = False
        zone.volume -= 1
        return f"Ship {ship.name} successfully participated in zone {zone.code}."

    def remove_battleship(self, ship_name: str):
        ship = next((s for s in self.ships if s.name == ship_name), None)
        if not ship:
            return "No ship with this name!"
        if not ship.is_available:
            return "The ship participates in zone battles! Removal is impossible!"

        self.ships.remove(ship)
        return f"Successfully removed ship {ship_name}."

    def start_battle(self, zone: BaseZone):
        attacker = max((s for s in zone.ships if s.is_attacking), key=lambda s: s.hit_strength, default=None)
        target = max((s for s in zone.ships if not s.is_attacking), key=lambda s: s.health, default=None)

        if not attacker or not target:
            return "Not enough participants. The battle is canceled."

        attacker.attack()
        target.take_damage(attacker)

        if target.health <= 0:
            zone.ships.remove(target)
            self.ships.remove(target)
            return f"{target.name} lost the battle and was sunk."

        if attacker.ammunition <= 0:
            zone.ships.remove(attacker)
            self.ships.remove(attacker)
            return f"{attacker.name} ran out of ammunition and leaves."

        return "Both ships survived the battle."

    def get_statistics(self):
        available_ships = [s for s in self.ships if s.is_available]
        available_ships_str = ', '.join(s.name for s in available_ships) if available_ships else ''

        zones_info = '\n'.join(zone.zone_info() for zone in sorted(self.zones, key=lambda z: z.code))

        result = f"Available Battleships: {len(available_ships)}\n"
        result += f"#{available_ships_str}#\n" if available_ships else ''
        result += (f"***Zones Statistics:***\n"
                   f"Total Zones: {len(self.zones)}"
                   f"\n{zones_info}")

        return result.strip()

