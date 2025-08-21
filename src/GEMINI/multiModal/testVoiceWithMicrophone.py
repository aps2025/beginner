import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

try:
    with sr.Microphone() as source:
        print("🎙️ Speak now...")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
        query = recognizer.recognize_google(audio)
        print("You said:", query)
        speak("You said " + query)
except sr.WaitTimeoutError:
    print("⚠️ Timeout: No speech detected.")
    speak("I didn't hear anything.")
except sr.UnknownValueError:
    print("🤷 Could not understand audio.")
    speak("Sorry, I didn't catch that.")
except Exception as e:
    print("🚨 Error:", e)
    speak("Something went wrong.")
finally:
    engine.stop()
