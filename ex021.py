import pygame

pygame.init()
pygame.mixer.music.load('runaway.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input()