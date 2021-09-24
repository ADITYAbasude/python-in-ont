import wikipedia
import pyttsx3
# import translator

while(True):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    a = input("Enter = ")

    def speak (audio) :
        engine.say(audio)


        
        engine.runAndWait()


    if __name__ == "__main__" :
        print(wikipedia.summary(a))
        speak(wikipedia.summary(a))
    
    
