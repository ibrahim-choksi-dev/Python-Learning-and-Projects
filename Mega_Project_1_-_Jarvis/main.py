import speech_recognition as sr
import webbrowser
import pyttsx3  # text-to-speech library
import music_library
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "YOUR_NEWS_API_KEY_HERE"


def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('output.mp3')

    pygame.mixer.init()
    pygame.mixer.music.load('output.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    os.remove('output.mp3')

def aiProcess(command):
    client = OpenAI(
    api_key="YOUR_OPENAI_API_KEY_HERE"
)
    completion = client.chat.completions.create(
    model="gpt-5.5",
    messages=[
        {
            "role": "system",
            "content": "You are a virtual assistant named Jarvis. Skilled in general tasks like Alexa and Google Cloud. Give short and correct responses. If you don't know the answer, say 'I don't know'."
        },
        {
            "role": "user",
            "content": command
        }
    ]
)

    return completion.choices[0].message.content


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")

    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = music_library.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            for article in articles[:5]:  # Get top 5 news articles
                speak_old(article["title"])

    else:
        #Let OpenAI handle the request
        output = aiProcess(c)
        speak_old(output)




if __name__ == "__main__":
    speak_old("Initializing Jarvis.....")

while True:
    # Listen for the wake word "Jarvis"
    # Listen for audio from the microphone
    r = sr.Recognizer()
    print("Recognizing....")

    try:
        with sr.Microphone() as source:
            print("Listening....")
            audio = r.listen(source, timeout=5, phrase_time_limit=5)

        word = r.recognize_google(audio)

        if word.lower() == "jarvis":
            speak_old("Ya")

            # Listen for command
            with sr.Microphone() as source:
                print("Jarvis Activated....")
                audio = r.listen(source)

            command = r.recognize_google(audio)
            processCommand(command)

    except Exception as e:
        print(type(e))
        print("Error, {0}".format(e))