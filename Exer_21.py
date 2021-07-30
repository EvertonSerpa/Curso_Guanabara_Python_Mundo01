'''Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.'''
print()
from pygame import mixer # importando o a função mixer da biblioteca pygamer

mixer.init() # iniciando o mixer
mixer.music.load('the_white_stripes_seven_nation_army.mp3') # carregando a musica
mixer.music.play() # dando play na musica

import time # import biblioteca time
time.sleep(360) # velocidade de reprodução..