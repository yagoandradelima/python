#Aula08 - Desafio 021 - TOCANDO UM MP3
#Esse desafio tentei fazer, mas não soube identificar como usar o módulo
#vou acompanhar a resolução do professor

import pygame
pygame.init()
pygame.mixer.music.load('1.mp3')
pygame.mixer.music.play()
pygame.event.wait()

#A música não funcionou muito bem, acho que foi o arquivo