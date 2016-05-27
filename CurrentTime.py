#!/bin/python
# -*- coding: utf-8 -*-
from gtts import gTTS
import time

time = "The Current Time is " + time.strftime("%I %M %p")
tts = gTTS(text=time, lang='en')
tts.save("/mnt/ram/temp.mp3")

print subprocess.call ('mpg123 -g 100 -h 10 -d 11 /mnt/ram/*.mp3', shell=True)

print 'cleaning up now'
      print subprocess.call ('rm /mnt/ram/*.mp3', shell=True)