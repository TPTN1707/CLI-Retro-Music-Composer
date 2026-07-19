

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