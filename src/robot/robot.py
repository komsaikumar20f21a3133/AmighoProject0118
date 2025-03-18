import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    print(f"Speaking: {audio}")
    if not engine._inLoop:
        engine.say(audio)
        engine.runAndWait()
    else:
        engine.endLoop()
        engine.say(audio)
        engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir!")   
    else:
        speak("Good Evening sir!")  
    speak("hi omsai, I am amigho Sir. Please tell me how may I help you")       

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")  
        return "None"
    return query

def handleCommand():
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'play music' in query:
            music_dir = 'F:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open gallery' in query:
            photos = "C:\\Users\\DELL\\OneDrive\\Desktop\\saiphoto.jpeg"
            os.startfile(photos)

        elif 'open email' in query:
            speak("opening email...")
            webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")

        elif 'open darknet' in query:
            speak("opening darknet sir....")
            webbrowser.open("https://www.darknetgame.com/")

        elif 'thank you' in query:
            speak("most welcome sir....")

        elif 'what doing ' in query:
            speak("nothing sir.... checking the google updates..")

        elif 'what the update' in query:
            speak("nothing much update sir... ")

        elif 'shutdown' in query:
            speak("i am shutting down sir....")

        elif 'open whatsapp' in query:
            speak("opening whatsapp...")
            print("opening whatsapp.....")
            webbrowser.open("https://web.whatsapp.com/")