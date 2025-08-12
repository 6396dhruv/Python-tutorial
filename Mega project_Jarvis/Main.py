import speech_recognition as sr #speech recognition 
import webbrowser # using web browser
import pyttsx3 # text to speech
import pocketsphinx
import MusicLibrary

recogniser = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = MusicLibrary.music[song]
        webbrowser.open(link)
    pass

if __name__ == "__main__":
    speak("Initializing jarvis...")
    # only listen for the word jarvis
    while True:
        r = sr.Recognizer()

        print("recognising...")
        
        # recognise speech using sphinx
        try:
            with sr.Microphone() as source:
                print("Listning...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("yaa")
            # listen for command
            with sr.Microphone() as source:
                print("jarvis active...")
                audio = r.listen(source)
                command = r.recognize_google(audio)

                processcommand(command)

        except Exception as e:
            print("Error; {0}".format(e))


        








