import pygame

pygame.mixer.init()
pygame.mixer.music.load("alarm.mp3")

def start_playing():
    pygame.mixer.music.play()

def stop_playing():
    pygame.mixer.music.stop()

if __name__ == '__main__':
    start_playing()
    input("Press Enter to stop...")  
    stop_playing()
