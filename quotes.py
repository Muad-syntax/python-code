import time
import sys


lyrics = [
    ("\nDi tengah badai yang mengamuk", 0.09),
    ("Dunia berguncang, jiwa meronta", 0.10),
    ("Api kebencian membakar hati", 0.10),
    ("Semuanya runtuh, tak ada lagi arti", 0.11),
    ("", 0.5),
    ("Bayang-bayang kesunyian menyergap", 0.10),
    ("Dunia menjadi kosong, tanpa nafas", 0.10),
    ("Hati yang terluka, tak bisa bernafas", 0.10),
    ("Menangis dalam diam, tanpa suara", 0.10),
    ("", 0.5),
    ("Dikala keputusasaan", 0.10),
    ("Secercah cahaya bersinar", 0.10),
    ("Api harapan tak pernah padam", 0.10),
    ("Membakar semangat, jiwa yang tak tamat", 0.10),
    ("", 0.5),
    ("Kita bangkit, meski terluka parah", 0.10),
    ("Kita melawan, meski badai mengamuk", 0.10),
    ("Kita mencari jalan, meski dalam kegelapan", 0.10),
    ("Kita berharap, meski semuanya runtuh", 0.10),
    ("", 0.5),
    ("Pusisi ini menggambarkan tema perjuangan dan harapan di tengah kesulitan dan keputusasaan.", 0.10),
    ("Meskipun dunia tampak gelap dan sunyi, namun ada secercah cahaya harapan yang membakar semangat untuk bangkit dan melawan", 0.10),
    ("", 0.5)
]

delays = [1.5, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1]

def animate_text(text, char_delay):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(char_delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def main():
    for i, (text, char_delay) in enumerate(lyrics):
        animate_text(text, char_delay)
        if i < len(lyrics) - 1:
            # Calculate the time until the next line should start
            next_line_delay = max(0, delays[i] - len(text) * char_delay)
            time.sleep(next_line_delay)

if __name__ == "__main__":
    main()