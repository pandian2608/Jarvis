import os
import pyttsx3
import eel

from engine.features import *
from engine.command import *

def start():
    
    eel.init("www")

    playAssistantSound()
    # Code to start Jarvis
    print("Jarvis is starting...")
    
    # Add speech synthesis code here
    engine = pyttsx3.init()
    engine.say("Hello, sir")
    engine.runAndWait()


    os.system('start msedge.exe --app="http://localhost:8000/index.html"')

    eel.start('index.html', mode=None, host='localhost', block=True)
