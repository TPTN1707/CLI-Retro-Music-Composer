

def parse_song_string(song_string):
    """Parses a space-separated song string into a list of (note, duration_factor) tuples.

    Example: "C4:1 D4:2" -> [("C4", 1.0), ("D4", 2.0)]
    """
    parsed_notes = []

    for token in song_string.split():
        if ":" in token:
            note, duration = token.split(":")
            duration = float(duration)
        else:
            note = token
            duration = 1.0  # Default duration factor if not specified

        parsed_notes.append((note, duration))

    return parsed_notes


def load_song_from_file(file_path):
    """Reads a song from a .txt file, ignoring empty lines and comments starting with '#'."""
    song_lines = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            cleaned_line = line.strip()
            # Skip empty lines and comment lines
            if cleaned_line and not cleaned_line.startswith("#"):
                song_lines.append(cleaned_line)

    # Combine all lines into a single space-separated song string
    return " ".join(song_lines)