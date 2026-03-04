from project.room import Room

class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: 'Room'):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        self.rooms[room_number - 1].take_room(people)

    def free_room(self, room_number: int):
        self.rooms[room_number - 1].free_room()

    def status(self):
        self.guests = sum(r.guests for r in self.rooms)
        result = [f"Hotel {self.name} has {self.guests} total guests"]
        free_rooms = [r.number for r in self.rooms if not r.is_taken]
        result.append(f"Free rooms: {', '.join(str(r) for r in free_rooms)}")
        taken_rooms = [r.number for r in self.rooms if r.is_taken]
        result.append(f"Taken rooms: {', '.join(str(r) for r in taken_rooms)}")
        return '\n'.join(result)
