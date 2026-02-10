import os
import webbrowser
import datetime
import sys
import time
import pyttsx3
import speech_recognition as sr
import sounddevice as sd

# ---------- SPEAK (REINIT SAFE) ----------
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 165)
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    time.sleep(0.2)

# ---------- LISTEN ----------
def listen():
    recognizer = sr.Recognizer()
    samplerate = 16000
    duration = 4  # seconds

    print("🎤 Listening...")
    recording = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=1,
        dtype="int16"
    )
    sd.wait()

    audio = sr.AudioData(recording.tobytes(), samplerate, 2)

    try:
        query = recognizer.recognize_google(audio)
        print("You:", query)
        return query.lower()
    except:
        return ""

# ---------- WISH ----------
def wish_me():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning sir")
    elif hour < 18:
        speak("Good afternoon sir")
    else:
        speak("Good evening sir")
    speak("Jarvis online. Speak your command.")

# ---------- START ----------
wish_me()

while True:
    query = listen()

    if not query:
        continue

    if "time" in query:
        speak(datetime.datetime.now().strftime("%I:%M %p"))

    elif "date" in query:
        speak(datetime.datetime.now().strftime("%d %B %Y"))

    elif "open google" in query:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in query:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open notepad" in query:
        speak("Opening Notepad")
        os.system("notepad")

    elif "close notepad" in query:
        speak("Closing Notepad")
        os.system("taskkill /f /im notepad.exe")

    elif "exit" in query or "bye" in query:
        speak("Goodbye sir")
        sys.exit()

    else:
        speak("Searching on Google")
        webbrowser.open("https://www.google.com/search?q=" + query)
def listen():
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 0.6
    recognizer.energy_threshold = 300

    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.3)
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

    try:
        query = recognizer.recognize_google(audio)
        print("You:", query)
        return query.lower()
    except:
        return ""
