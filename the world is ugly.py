import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("But you'll never fight alone", 0.1),
        ("'Cause I wanted you to knoooowww", 0.1),
        ("That the world is ugly", 0.1),
        ("But you're beautiful to me", 0.1),
        ("Well are you thinking of me now", 0.12),
    ]
    delays = [0.3, 5.0, 10.0, 15.0, 19.0]  
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()
