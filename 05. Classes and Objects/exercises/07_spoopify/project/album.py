from .song import Song

class Album:
    def __init__(self, name: str, *song: Song):
        self.name = name
        self.published = False
        self.songs: list[Song] = [s for s in song]

    def add_song(self, song: Song):
        if self.published:
            return "Cannot add songs. Album is published."
        elif song.single:
            return f"Cannot add {song.name}. It's a single"
        elif song in self.songs:
            return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."
        
        song_to_remove = next((s for s in self.songs if s.name == song_name), None)
        if song_to_remove is None:
            return "Song is not in the album."
        
        self.songs.remove(song_to_remove)
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        return f"Album {self.name} is already published."

    def details(self):
        album_info = [f"Album {self.name}"]
        for song in self.songs:
            album_info.append(f"== {song.get_info()}")
        return '\n'.join(album_info)
