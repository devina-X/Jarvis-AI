import speech_recognition as sr
from langdetect import detect


def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for noise...")
        r.adjust_for_ambient_noise(source, duration=1)

        print("Listening...")
        audio = r.listen(source)

        try:
            print("Recognizing...")

            # 🌍 Use English as base (works best for mixed speech)
            query = r.recognize_google(audio, language="en-in")
            print("You said:", query)

            # 🔍 Detect language from text
            try:
                lang = detect(query)
                print("Detected language:", lang)
            except:
                lang = "unknown"

            return query.lower(), lang

        except Exception as e:
            print("Error:", e)
            return "", "unknown"