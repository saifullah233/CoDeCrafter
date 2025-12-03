import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import webbrowser
import os

# Initialize the voice engine
engine = pyttsx3.init()
engine.setProperty('rate', 180)  # speaking speed
engine.setProperty('volume', 1.0)  # volume level

def speak(text):
    """Speak out the given text"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to user's voice and convert it to text"""
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        listener.pause_threshold = 1
        audio = listener.listen(source)
    try:
        print("Recognizing...")
        command = listener.recognize_google(audio, language='en-in')
        print(f"You said: {command}\n")
    except Exception as e:
        speak("Sorry, I didn't catch that. Please say it again.")
        return ""
    return command.lower()

def wish_me():
    """Wish user according to time"""
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your voice assistant. How can I help you today?")

def run_assistant():
    """Main logic of Jarvis"""
    wish_me()
    while True:
        command = listen()

        if 'wikipedia' in command:
            speak('Searching Wikipedia...')
            query = command.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'play' in command:
            song = command.replace('play', '')
            speak('Playing ' + song)
            pywhatkit.playonyt(song)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('The current time is ' + time)

        elif 'open google' in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif 'open youtube' in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
        elif' open chrome' in command:
            speak("Opening Chrome")
            webbrowser.open("C:/Program Files/Google/Chrome/Application/chrome.exe")
        elif 'open facebook' in command:
            speak("Opening Facebook")
            webbrowser.open("https://www.facebook.com")

        elif 'open twitter' in command:
            speak("Opening Twitter")
            webbrowser.open("https://www.twitter.com")
        elif' open github' in command:
            speak("Opening GitHub")
            webbrowser.open("https://www.github.com")
        elif'open whatsapp' in command:
            speak("Opening WhatsApp")
            webbrowser.open("https://web.whatsapp.com")

        elif 'open instagram' in command:
            speak("Opening Instagram")
            webbrowser.open("https://www.instagram.com")

        elif 'open notepad' in command:
            speak("Opening Notepad")
            os.system("notepad.exe")

        elif 'exit' in command or 'stop' in command:
            print("Goodbye! Have a nice day.")
            break
        else:
            speak("I can’t do that yet, but I’m learning!")

# Run the assistant
run_assistant()

