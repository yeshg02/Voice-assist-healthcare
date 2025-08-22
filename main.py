import os
from dotenv import load_dotenv
from openai import OpenAI
import speech_recognition as sr
import pyttsx3

load_dotenv()  # Load .env file

API_KEY = os.getenv("OPENAI_API_KEY")

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)

def ai(userquery):
    try:
        client = OpenAI(api_key=API_KEY)
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
        say(''.join(generated_texts))
        print(''.join(generated_texts))
    except Exception as e:
        print(e)

def say(text):
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language="en-in")
        print("User said:", query)
        say(query)
        return query
    except Exception:
        return "Can You try saying once again!!"

if __name__ == '__main__':
    while True:
        print("Listening...")
        query = takecommand()
        if "alpha" in query.lower():
            query = query.lower().replace('alpha', "Health-AI")
            ai(userquery=query)
