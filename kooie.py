import os
import webbrowser
import wikipedia
import pyttsx3
import datetime
import speech_recognition as sr



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice' ,voices[0].id)

def speak (audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning khushi")

    elif hour>=12 and hour < 18:
        speak("Good Afternoon khushi")

    else:
        speak("Good night khushi")
    speak (" Iam kookie  madam, please tell me how can I help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        speak("listening")
        r.pause_threshold =1
        audio = r.listen(source) 

    try:
        print("Recogniseing.....")
        speak("Recogniseing.....")
        query = r.recognize_google(audio, language ='en-in')
        print(f"user said : { query}\n")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         


    except Exception  as e :
        print("say that again madam.")
        speak("say that again madam.")
        return "None"
    return query

if __name__ == "__main__" :

    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak ('searching wikkipedia....')
            query = query.replace('wilipedia','')
            results= wikipedia.summary(query, sentences=2)
            speak ('According to wikipedia')
            print(results)
            speak(results)
        elif 'open youtube' in query:
                webbrowser.open("youtube.com")
        elif 'open google' in query :
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query :
            webbrowser.open ('stackoverflow.com')
        elif ' the time' in query :
                strtime = datetime.datetime.now().strtime('%f %m %s')
                speak(f"time is {strtime}\n")
        
                
    









