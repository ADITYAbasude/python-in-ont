# import pyttsx3
import datetime

try:
    pass
    import pyttsx3
except Exception as e:
    print(e)


engine = pyttsx3.init('sapi5')
voice = engine.get.property('voice')
print(voice[1].id)
engine.setProperty('voice',voice[1].id)

def speak(audio):
    engine.say(audio)    
    engine.runandwait() 

hour = int(datetime.datetime.now().hour)

if (hour >= 0 and hour >= 12):
    speak("Good morning")
