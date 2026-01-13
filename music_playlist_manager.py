class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration  # seconds

    def __repr__(self):
        return f"{self.title} by {self.artist} ({self.duration}s)"


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song_title):
        self.songs = [song for song in self.songs if song.title != song_title]

    def get_total_duration(self):
        return sum(song.duration for song in self.songs)

    def list_songs(self):
        return self.songs


# ---- Main Program ----
def main():
    song1 = Song("God's Plan", "Drake", 198)
    song2 = Song("Hello", "Adele", 295)
    song3 = Song("Water", "Tyla", 180)
    song4 = Song("Last Last", "Burna Boy", 210)
    song5 = Song("Halo", "Beyonce", 261)
    song6 = Song("Free Mind", "Tems", 240)

    playlist1 = Playlist("My Favorites")

    for song in (song1, song2, song3, song4, song5, song6):
        playlist1.add_song(song)

    print(f"\nPlaylist: {playlist1.name}")
    print("Songs:")
    for song in playlist1.list_songs():
        print(f"- {song}")

    print(f"\nTotal duration: {playlist1.get_total_duration()} seconds")


main()
