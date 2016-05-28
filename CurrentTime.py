#!/bin/python
# -*- coding: utf-8 -*-
import time
import pyvona
import pygame
import subprocess

#Creates Time variable
time = time.strftime("%I %M %p")
time = list(time)

if time[0][0] == "0":
	time.pop(0)
	time = ''.join(time)
else:
	time = ''.join(time)

time = "The Current Time is " + time
v = pyvona.create_voice('GDNAJW3FDVSMQKUCCFKQ','RoXbQ1VnTPU/dvmzhSwx43mjnXhBzlEeMc2qoNcu')
#Settings for ivona
v.voice_name = 'Brian'
v.speech_rate = 'slow'
#Get ogg file with speech
v.fetch_voice(time, '/mnt/ram/tempspeech.ogg')


pygame.mixer.init()
pygame.mixer.music.load("/mnt/ram/tempspeech.ogg")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue

print 'cleaning up now'
print subprocess.call ('rm /mnt/ram/*.ogg', shell=True)