import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser

engine = pyttsx3.init()

def listen():
    fs = 44100
    duration = 5

    print("Speak now...")

    recording = sd.rec(
        int(duration * fs),
        samplerate=fs,
        channels=1,
        dtype='int16'
    )

    sd.wait()

    write("temp.wav", fs, recording)

    r = sr.Recognizer()

    with sr.AudioFile("temp.wav") as source:
        audio = r.record(source)

    return r.recognize_google(audio)


def processCommand(cmd):
    response = ""
    if "open google" in cmd:
        response = "Opening Google"
        webbrowser.open("https://www.google.com")
    elif "what time is it" in cmd:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        response ="The current time is {}".format(current_time)
    elif "linkedin" in cmd:
        response = "Opening LinkedIn"
        webbrowser.open("https://www.linkedin.com")
    else:
        response = "Command not recognized"
    engine.say(response)
    engine.runAndWait()
    print(f"Reply: {response}")

while True:
    try:
        text = listen()
        if(text!=""):
            processCommand(text.lower())
            print("\n\n\nYou said:", text)
    except Exception as e:
        print("Error:", e)