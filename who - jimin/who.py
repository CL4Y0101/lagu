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
    pygame.mixer.music.load("who-jimin.mp3")
    pygame.mixer.music.play()

 
    lyrics = [
        ("We never met, but he's all I see at night", 0.1),
        ("Never met, but he's always on my mind", 0.1),
        ("Wanna give him the world and so much more", 0.11),
        ("Who is my heart waiting for?", 0.08),
        ("Is he someone that I see every day?", 0.1),
        ("Is he somewhere a thousand miles away?", 0.12),
        ("Wanna give him the world and so much more", 0.1),
        ("Who is my heart waiting for?", 0.1),
        ("DAMNNN", 0.1)
    ]

   
    delays = [0.9, 5.5, 7.8, 15.5, 17.5, 20.0, 24.0, 31.5, 34.0]


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
