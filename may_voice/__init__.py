from TTS.api import TTS

from os import environ
environ ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame,sys,time

pygame.mixer.init()

pygame.mixer.music.load('prueba.wav')

while(True):
    opc = input("opcion: ")
    if opc == 'pausa':
        pygame.mixer.music.pause()
    elif opc == 'stop':
        pygame.mixer.music.stop()
        break
    elif opc=='play':
        pygame.mixer.music.play()
    elif opc=='unpause':
        pygame.mixer.music.unpause()
