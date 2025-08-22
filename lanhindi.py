import os
from dotenv import load_dotenv
import pyttsx3
from openai import OpenAI
import speech_recognition as sr

load_dotenv()  # Load .env file

engine = None
voices = None

def init_engine():
    global engine, voices
    if engine is None:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')

def say(text):
    init_engine()
    engine.setProperty('voice', voices[3].id)
    engine.say(text)
    engine.runAndWait()

def speak(text):
    init_engine()
    engine.setProperty('voice', voices.id)
    engine.setProperty('rate', 180)
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

def ai(userquery):
    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[{"role": "user", "content": userquery}],
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        generated_texts = [choice.message.content for choice in response.choices]
        res = ''.join(generated_texts)
        print("ai", res)
        return res
    except Exception as e:
        print(e)
