from .album import Album

class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums: list[Album] = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        album_to_remove = next((a for a in self.albums if a.name == album_name), None)
        if album_to_remove is None:
            return f"Album {album_name} is not found."
        elif album_to_remove.published:
            return "Album has been published. It cannot be removed."
        self.albums.remove(album_to_remove)
        return f"Album {album_name} has been removed."

    def details(self):
        band_info = [f"Band {self.name}"]
        for album in self.albums:
            band_info.append(album.details())
        return '\n'.join(band_info)


# Test code
# song = Song("Running in the 90s", 3.45, False)
# print(song.get_info())
# album = Album("Initial D", song)
# second_song = Song("Around the World", 2.34, False)
# print(album.add_song(second_song))
# print(album.details())
# print(album.publish())
# band = Band("Manuel")
# print(band.add_album(album))
# print(band.remove_album("Initial D"))
# print(band.details())