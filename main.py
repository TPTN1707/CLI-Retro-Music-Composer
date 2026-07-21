import os
from src.cli import get_user_choice, show_menu
from src.parser import load_song_from_file, parse_song_string
from src.player import play_tone


def play_song(song_string, base_speed=300):
    """Orchestrates the parser and player modules to play an entire song."""
    notes = parse_song_string(song_string)

    for note_name, duration_factor in notes:
        duration_ms = int(base_speed * duration_factor)
        play_tone(note_name, duration_ms)


def play_song_from_directory(songs_dir="songs"):
    """Lists files in songs directory and plays the user's selected file."""
    if not os.path.exists(songs_dir) or not os.path.isdir(songs_dir):
        print(f"\nError: Directory '{songs_dir}' does not exist.")
        return

    # Filter out only .txt files
    song_files = [f for f in os.listdir(songs_dir) if f.endswith(".txt")]

    if not song_files:
        print(f"\nNo .txt song files found in '{songs_dir}' directory.")
        return

    # Display list of available song files
    print("\n--- Available Songs ---")
    for index, filename in enumerate(song_files, start=1):
        print(f"{index}. {filename}")

    try:
        selection = int(input("\nSelect a song number to play: "))
        if 1 <= selection <= len(song_files):
            selected_file = song_files[selection - 1]
            file_path = os.path.join(songs_dir, selected_file)

            # Load and play the selected song
            print(f"\nLoading and playing: {selected_file}...")
            song_content = load_song_from_file(file_path)
            play_song(song_content)
        else:
            print("\nInvalid song number.")
    except ValueError:
        print("\nPlease enter a valid number.")


def main():
    while True:
        show_menu()
        choice = get_user_choice()

        if choice == "1":
            sample_song = "C4:1 D4:1 E4:1 C4:1 E4:1 C4:1 G4:2"
            print("\nPlaying sample song...")
            play_song(sample_song)

        elif choice == "2":
            user_song = input(
                "\nEnter song string (e.g., C4:1 E4:1 G4:2): "
            ).strip()
            if user_song:
                print("\nPlaying your custom song...")
                play_song(user_song)

        elif choice == "3":
            play_song_from_directory()

        elif choice == "4":
            print("\nLive Keyboard Piano Mode is under development.")

        elif choice == "5":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid option. Please try again.")


if __name__ == "__main__":
    main()