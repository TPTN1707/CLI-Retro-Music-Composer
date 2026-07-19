import time
import winsound

# Frequencies for musical notes in octaves 4 and 5
NOTE_FREQS = {
    "C4": 261,
    "D4": 294,
    "E4": 329,
    "F4": 349,
    "G4": 392,
    "A4": 440,
    "B4": 493,
    "C5": 523,
    "D5": 587,
    "E5": 659,
    "R": 0,  # Rest note (silent)
}


def play_tone(note_name, duration_ms):
    """Plays a specific musical note for a given duration in milliseconds."""
    freq = NOTE_FREQS.get(note_name, 0)

    if freq == 0 or note_name == "R":
        # Pause the execution for rest notes or invalid inputs
        time.sleep(duration_ms / 1000)
    else:
        # Generate the beep sound
        winsound.Beep(freq, duration_ms)