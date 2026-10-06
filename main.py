import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "6fe2aa43c7fd404c9b580e1753808624"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
            webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get( "https://newsapi.org/v2/top-headlines?country=us&apiKey=6fe2aa43c7fd404c9b580e1753808624" ) 
        if r.status_code == 200:
            data = r.json() 
            articles = data.get("articles", []) 
            if articles: 
                print("Today's Top Headlines:") 

                for article in articles:
                    headline = article.get("title") 

                    if headline: 
                        print(headline) 
                        speak(headline) 
            else:
                print("No news articles found.")

                    
        else:
            print("Failed to fetch news.") 
            print("Status Code:", r.status_code)

    
    


if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        r = sr.Recognizer()
        
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=3, phrase_time_limit=2)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                 speak("Ya")
                 #Listen for commands
                 with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
                 
        except Exception as e:
            print("Error; {0}".format(e))


