import pygame
import os

pygame.init()
screen = pygame.display.set_mode((800 , 800))

playlist = [
    "Billie Eilish - WILDFLOWER.mp3",
    "Billie Eilish - Bad Guy.mp3",
    "Billie Eilish - all the good girls go to hell.mp3"

]
current_track = 0
def play_music():
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()
play_music()
running = True
pause = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    pause = True
                else:
                    pygame.mixer.music.unpause()
                    pause = False
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
            elif event.key == pygame.K_n:
                current_track = (current_track + 1) % len(playlist)
                play_music()
            elif event.key == pygame.K_p:
                 current_track = (current_track - 1) % len(playlist)
                 play_music()

            elif event.key == pygame.K_ESCAPE:
                running = False
pygame.quit()















