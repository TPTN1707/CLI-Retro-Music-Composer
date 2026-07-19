from src.cli import get_user_choice, show_menu
from src.parser import parse_song_string
from src.player import play_tone


def play_song(song_string, base_speed=300):
    """Orchestrates the parser and player modules to play an entire song."""
    notes = parse_song_string(song_string)

    for note_name, duration_factor in notes:
        duration_ms = int(base_speed * duration_factor)
        play_tone(note_name, duration_ms)


def main():
    while True:
        show_menu()
        choice = get_user_choice()

        if choice == "1":
            # Play a simple built-in melody
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
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid option. Please try again.")


if __name__ == "__main__":
    main()