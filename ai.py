import openai
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

# 🔑 Put your OpenAI API key here
openai.api_key = "AIzaSyCqTqH_im-MGuSm2hxxHz2h6qETmMXzepg"

# Voice Engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    print("AI:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print("You:", command)
            return command
        except:
            return ""

def ask_ai(question):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": question}]
    )
    return response['choices'][0]['message']['content']

# Main Loop
speak("Powerful AI Activated")

while True:
    command = listen().lower()

    if "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak("The time is " + time)

    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    elif "exit" in command:
        speak("Shutting down")
        break

    else:
        answer = ask_ai(command)
        speak(answer)






        
