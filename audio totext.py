from time import time
from tracemalloc import take_snapshot
from speech_recognition import speech_recognition
import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyaudio
import datetime

listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk():
       engine.say(text)
       engine.runandwait()

def  take.command:
               
try:
           with sr.microphone() as source:
               print('listening....')
               voice=listener.listen(source)
               command=listener.recgnize_google(voice)
               command=command.voice()
               if 'skill' in command:
                   command=command.replace('skill','')
                   print(command)
except:
      pass
return

def run_skill() :
    command=talk.command()
    if'play' in command:
        command=command.replace('play','')
        talk('playing'+song,read)
        pywhatkit.playonyt(song)   
    elif 'time' in command:
        time=datetime.datetime.now()    
        talk('current time is'+time)

run_skill()
