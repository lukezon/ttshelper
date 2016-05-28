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

#it won't work without this if statement, not sure why
if 1 == 1:
    #uses xml information to create service report
    mtaStatus=MTAStatus()
    timeMTA_ReportedData=mtaStatus.getReportTime()
    
    subwayDictionary=mtaStatus.getSubway()
    for name in sorted(subwayDictionary.keys()):
        #if orange line is good
        if subwayDictionary[name].getName() == "BDFM" and subwayDictionary[name].getStatus() == "GOOD SERVICE":
            #if orange line is good and blue line is good
            if subwayDictionary[name].getName() == "ACE" and subwayDictionary[name].getStatus() == "GOOD SERVICE":
                subwaystat = "Both the Blue and Orange lines have good service. "
                print "1"
            #if orange line is good but Blue is not good
            if subwayDictionary[name].getName() == "ACE" and not subwayDictionary[name].getStatus() == "GOOD SERVICE":
                subwaystat = "The Orange line has good service but the Blue line has %s." % (subwayDictionary[name].getStatus())
                print "2"
        #if Orange line is not good
        if subwayDictionary[name].getName() == "BDFM" and not subwayDictionary[name].getStatus() == "GOOD SERVICE":
            #if Orange line is not good and Blue is good
            if subwayDictionary[name].getName() == "ACE" and subwayDictionary[name].getStatus() == "GOOD SERVICE":
                subwaystat = "The blue line has good service but The Orange line has %s." % (subwayDictionary[name].getStatus())
                print "3"
            #if both the Orange and Blue lines are not good
            else:
                subwaystat = "There are problems with both the Blue and Orange lines."
                print "4"

                #This whole above section does not work because it cannot sort threw multiple subway lines at a time

    v = pyvona.create_voice('GDNAJW3FDVSMQKUCCFKQ','RoXbQ1VnTPU/dvmzhSwx43mjnXhBzlEeMc2qoNcu')
    #Settings for ivona
    v.voice_name = 'Brian'
    v.speech_rate = 'slow'
    #Get ogg file with speech
    v.fetch_voice(subwaystat, '/mnt/ram/tempspeech.ogg')


    pygame.mixer.init()
    pygame.mixer.music.load("/mnt/ram/tempspeech.ogg")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

print 'cleaning up now'
print subprocess.call ('rm /mnt/ram/*.ogg', shell=True)
