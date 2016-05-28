#!/bin/python
# -*- coding: utf-8 -*-
import urllib
from lxml import etree
import os
import os, glob
import datetime
import logging
import feedparser
import pyvona
import pygame
import subprocess

class MTA(object):
    '''class to hold data about a NYC MTA line'''
    def __init__(self, name, status, text, date, time):
        '''data attributes are named same as XML attributes'''
        self.name=name
        self.status=status
        self.text=text
        self.date=date
        self.time=time
    def getName(self):
        return self.name
    def getStatus(self):
        return self.status
    def getText(self):
        return self.text
    def getDate(self):
        return self.date
    def getTime(self):
        return self.time
    def getMode(self):
        return self.mode

class Subway(MTA):
    '''class to hold data about a NYC Subway line'''
    def __init__(self, name, status, text, date, time):
        super(Subway, self).__init__(name, status, text, date, time)
        self.Mode='subway'
    
class MTAStatus():

    def __init__(self):
        url='http://web.mta.info/status/serviceStatus.txt'
        self.subwayDataAsXML=urllib.urlopen(url).read()
        #open('subwayData.xml', "w").write(xmlData)
        self.root = etree.XML(self.subwayDataAsXML)

                # uncomment to write XML data for later reference
                    #debugXMLfile = "xml\\mta_%s.xml" % (datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
                    #open(debugXMLfile,"w").write(self.subwayDataAsXML)
                    #logging.debug('firefox.exe %s\\%s' % (os.getcwd(), debugXMLfile) )

        # get MTA metadata
        self.responseCode = self.root.xpath('responsecode')[0].text
        self.timeStamp = self.root.xpath('timestamp')[0].text
    def getReportTime(self):
        return self.timeStamp
    def getSubway(self):
        '''Subway data'''
        self.subwayDict = {}    
        # iterate through XML data, only care about Subway data for now
        for count in range(len(self.root.xpath('subway/line/name'))):
            name = self.root.xpath('subway/line/name')[count].text
            status = self.root.xpath('subway/line/status')[count].text
            text = self.root.xpath('subway/line/text')[count].text
            date = self.root.xpath('subway/line/Date')[count].text    
            time = self.root.xpath('subway/line/Time')[count].text
            s = Subway(name, status, text, date, time)

            #s = Subway(self.root.xpath('subway'))
            self.subwayDict[s.getName()] = s
        return self.subwayDict


#uses xml information to create service report
mtaStatus=MTAStatus()
timeMTA_ReportedData=mtaStatus.getReportTime()

subwayDictionary=mtaStatus.getSubway()
for name in sorted(subwayDictionary.keys()):
    #creates report info for ACE line in varable ACEstat
    if subwayDictionary[name].getName() == "ACE":
        if subwayDictionary[name].getStatus() == "GOOD SERVICE":
            ACEstat = "good"
        else:
            ACEstat = "%s" % (subwayDictionary[name].getStatus())
    #creates report info for BDFM line in varable BDFMstat
    if subwayDictionary[name].getName() == "BDFM":
        if subwayDictionary[name].getStatus() == "GOOD SERVICE":
            BDFMstat = "good"
        else:
            BDFMstat = "%s" % (subwayDictionary[name].getStatus())

#print for debug
print BDFMstat
print ACEstat

#fixes grammer for ACE and BDFM stats
if ACEstat == "DELAYS":
    ACEstat = "are delays"
elif ACEstat == "SERVICE CHANGE":
    ACEstat = "are service changes"

if BDFMstat == "DELAYS":
    BDFMstat = "are delays"
elif BDFMstat == "SERVICE CHANGE":
    BDFMstat = "are service changes"

#print for debug
print BDFMstat
print ACEstat


#combines ACE and BDFM info into logical sentence
if ACEstat == "good" and BDFMstat == "good":
    subwaystat = "There are no problems with the Blue or Orange lines."
elif ACEstat == "good" and not BDFMstat == "good":
    subwaystat = "The Blue line has no problems but there %s on the Orange line." % BDFMstat
elif not ACEstat == "good" and BDFMstat == "good":
    subwaystat = "The Orange line has no problems but there %s on the Blue line." % ACEstat
elif not ACEstat == "good" and not BDFMstat == "good":
    if ACEstat == BDFMstat:
        subwaystat = "There %s on both the Blue and Orange lines." % ACEstat
    else:
        subwaystat = "There " + ACEstat + " on the Blue line and there " + BDFMstat + " the Orange line."
else:
    subwaystat = "There was an error reading the xml document."


#creates the speech file
v = pyvona.create_voice('GDNAJW3FDVSMQKUCCFKQ','RoXbQ1VnTPU/dvmzhSwx43mjnXhBzlEeMc2qoNcu')
#Settings for ivona
v.voice_name = 'Brian'
v.speech_rate = 'slow'
#Get ogg file with speech
v.fetch_voice(subwaystat, '/mnt/ram/tempspeech.ogg')

#plays the speech file
pygame.mixer.init()
pygame.mixer.music.load("/mnt/ram/tempspeech.ogg")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue

#cleans up the speech file
print 'cleaning up now'
print subprocess.call ('rm /mnt/ram/*.ogg', shell=True)