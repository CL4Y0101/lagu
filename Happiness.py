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
        ("When I turn 81 and forget things", 0.16),
        ("Will you still be prouuuuuuuuud?", 0.13),
        ("Proud of me, of my short list of accomplishments", 0.13),
        ("Me and my lack of new news...", 0.15),
        ("Me and my selfishness", 0.11),
        ("Or me and myself wish you nothing but a happy new version of you", 0.11),
    ]
    delays = [0.1, 6.0, 13.0, 21.0, 28.0, 32.0]  

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
