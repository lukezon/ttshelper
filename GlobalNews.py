#!/bin/python
# -*- coding: utf-8 -*-
import feedparser
import pyvona
import pygame
import subprocess

try: 
#get rss newsfeed
    rss = feedparser.parse('http://feeds.bbci.co.uk/news/world/rss.xml')
    newsfeed = rss.entries[0]['title'] + '. Description: ' + rss.entries[0]['description'] + '.  ' + rss.entries[1]['title'] + '. description: ' + rss.entries[1]['description'] + '.  ' + rss.entries[2]['title'] + '. description: ' + rss.entries[2]['description'] + '.  ' + rss.entries[3]['title'] + '. description: ' + rss.entries[3]['description'] + '.  ' 

# print newsfeed
    newsfeed = newsfeed.encode('utf-8')

# Today's news from BBC
    news = 'Here are the top three stories from BBC. ' + newsfeed
    

except rss.bozo:
    news = 'Failed to reach BBC News'

print news

#creates the speech file
v = pyvona.create_voice('GDNAJW3FDVSMQKUCCFKQ','RoXbQ1VnTPU/dvmzhSwx43mjnXhBzlEeMc2qoNcu')
#Settings for ivona
v.voice_name = 'Brian'
v.speech_rate = 'medium'
#Get ogg file with speech
v.fetch_voice(news, '/mnt/ram/tempspeech.ogg')

#plays the speech file
pygame.mixer.init()
pygame.mixer.music.load("/mnt/ram/tempspeech.ogg")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue

#cleans up the speech file
print 'cleaning up now'
print subprocess.call ('rm /mnt/ram/*.ogg', shell=True)