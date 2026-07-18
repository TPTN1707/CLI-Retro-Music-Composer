import time
import winsound

# Bảng tần số cơ bản của các nốt nhạc ở quãng tám thứ 4 (Octave 4)
NOTE_FREQS = {
    "C": 261,  # Đô
    "D": 294,  # Rê
    "E": 329,  # Mi
    "F": 349,  # Pha
    "G": 392,  # Sol
    "A": 440,  # La
    "B": 493,  # Si
    "C5": 523,  # Đô (quãng 5)
    "R": 0,  # Rest (Nốt lặng - không phát âm thanh)
}


def play_song(sheet_music, speed=300):
    """Phát một chuỗi nốt nhạc.

    speed: thời gian mỗi nốt (mili-giây)
    """
    for note in sheet_music.split():
        if note in NOTE_FREQS:
            freq = NOTE_FREQS[note]
            if freq == 0:
                time.sleep(speed / 1000)  
            else:
                winsound.Beep(freq, speed)
        else:
            print(
                f"Không nhận diện được nốt: {note}"
            ) 



song = "C D E C C D E C E F G R E F G"

print("Đang phát nhạc...")
play_song(song, speed=400)