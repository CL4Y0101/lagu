import time
from threading import Thread, Lock
import sys
import pygame
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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
    
    pygame.mixer.init()
    pygame.mixer.music.load("laufey.mp3")
    pygame.mixer.music.play()
    lyrics = [
        ("What's a girl to do?", 0.1),
        ("Lying on my bed, staring into the blue", 0.1),
        ("Unrequited, terrifying", 0.1),
        ("Love is driving me a bit insane", 0.15),
        ("Have to get this off my chest", 0.07),
        ("I'm telling you today", 0.1),
        ("That when I talk to you, oh, Cupid walks right through", 0.1),
        ("And shoots an arrow through my heart", 0.1),
        ("And I sound like a loon, but don't you feel it too?", 0.1),
        ("Confess I loved you from the start", 0.1),
        ("Confess I loved you from the start", 0.15),
        ("Nabilah Firna JLEK", 0.2)
    ]
    delays = [3.0, 6.0, 12.5, 15.0, 21.5, 22.5, 27.0, 30.2, 38.3, 41.4, 49.0, 52.0]
    
    clear_screen()
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

    pygame.mixer.music.stop()

if __name__ == "__main__":
    sing_song()