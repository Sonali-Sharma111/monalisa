import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library
import requests

recognizer= sr.Recognizer()
engine=pyttsx3.init()
newsapi="9b9503da9ca14aafb5c42ab5620c12b2"


def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split("")[1]
        link =music_library.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f" https://newsapi.org/v2/everything?q=Apple&from=2024-08-23&sortBy=popularity&apiKey=API_KEY={newsapi}")
        if r.status_code == 200:
            
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])
                
    else:
        
        
        # let open ai handle the request          #
        pass
    
    
if __name__=="__main__":
    speak("intializing monalisa....")
    while True:
        # listen for the wake word monalisa"
        # obtain audio from the microphone
        r = sr.Recognizer()
        print("Recognizing...")
          
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("listening..")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word= r.recognize_google(audio)
            if (word.lower() =="monalisa"):
                speak("ya")
                # listen for command
                with sr.Microphone() as source:
                    print("monalisa_active..")
                    audio = r.listen(source)
                    command= r.recognize_google(audio)
                    processcommand(command)
                
        except Exception as e:
            print(" Error; {0}".format(e))
   
 