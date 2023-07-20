class Song:
    def __init__(
        self,
        track: str,
        artist: str,
        genre: str,
        bpm: int,
        energy: int,
        danceability: int,
        length: int,
    ):
        self.track = track
        self.artist = artist
        self.genre = genre
        self.bpm = int(bpm)
        self.energy = int(energy)
        self.danceability = int(danceability)
        self.lenght = int(length)

    def __str__(self):
        return f"{self.track},{self.artist},{self.genre},{self.bpm},{self.energy},{self.danceability},{self.lenght}"

    def change_speed(self, relative_bpm: int) -> None:
        if relative_bpm > 0:
            self.bpm += relative_bpm
            self.energy += 2 * relative_bpm
            self.danceability += 3 * relative_bpm
            self.lenght -= relative_bpm
        elif relative_bpm < 0:
            self.bpm -= abs(relative_bpm)
            self.energy -= 2 * abs(relative_bpm)
            self.danceability -= 3 * abs(relative_bpm)
            self.lenght += abs(relative_bpm)

    @staticmethod
    def load_songs(path: str) -> list["Song"]:
        songs = []
        with open(path, "r") as f:
            for line in f:
                songs.append(Song(*line.strip().split(",")))
        return songs

    @staticmethod
    def save_songs(songs: list["Song"], path: str) -> None:
        with open(path, "w") as f:
            for song in songs:
                f.write(str(song) + "\n")
            f.close()


if __name__ == "__main__":
    pass
