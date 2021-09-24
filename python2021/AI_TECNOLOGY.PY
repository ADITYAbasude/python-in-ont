import pyttsx3
import smtplib
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import datetime


# import PyAudio

# a = input("Please enter = ")
engine = pyttsx3.init('sapi5')





voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id) 

def speak(audio):
    engine.say(audio)
    
    engine.runAndWait()



def say():
    time = int(datetime.datetime.now().hour)
    if time>=0 and time<12:
        speak("Good morning Aditya")

    elif time>=12 and time<17:
        speak("Good afternoon Aditya")

    elif time>=17 and time<19:
        
        speak("Good evining Aditya")

    elif time>=19 and time<24:
        speak("Good night Aditya")
    
def micro():
    mic = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning......!") 
        # mic.non_speaking_duration(1)
        audio = mic.listen(source)

    try :
        speak("Done")
        query = mic.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("Please try again")
        return "none"
    return query

if __name__ == "__main__":
    
    speak("Hello sir , How can i help you")   
    # bolo = micro().lower()
    # speak( f"Thanks to meet you {bolo}")

    Quiz = micro().lower()

    if "aditya" in Quiz:
        speak("You are aditya!")
        

    elif "open code" in Quiz:
        os.startfile("‪D:\\Microsoft VS Code\\Code.exe")

    elif "Who is Narendra Modi" in Quiz:
        wikipedia()
    # elif "play music" in Quiz:
    #     os.startfile("")

    elif "what is time now" in Quiz:
        datetime.datetime.now().strftime("%H %M %S")
 
    elif "open youtube" in Quiz:
        webbrowser.open("https://www.youtube.com/")
