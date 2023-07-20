import sys

from spotify import Song

if __name__ == "__main__":
    input_file = "top50.csv"
    output_file = "top50_mod.csv"
    valid_input = False
    while not valid_input:
        try:
            relative_bpm = int(sys.argv[1])
            valid_input = True
        except (ValueError, IndexError):
            print("Please enter a valid integer as a command line argument.")
            sys.exit(1)
    loaded_songs = Song.load_songs(input_file)
    for song in loaded_songs:
        song.change_speed(relative_bpm)
    Song.save_songs(loaded_songs, output_file)
