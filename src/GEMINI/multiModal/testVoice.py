import speech_recognition as sr
import pyttsx3
import google.generativeai as genai

 # Prevents __del__ errors

# Configure Gemini API
genai.configure(api_key="AIzaSyCqIlp7mTSarIsucoFy7snPp1uweso6T5w")
model = genai.GenerativeModel("gemini-2.5-pro")

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
tts = pyttsx3.init()

# Capture voice input
with sr.Microphone() as source:
    print("🎙️ Speak now...")
    print(source)
    try:
        audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
        print(f"🔊 Listening...{audio}")
    except sr.WaitTimeoutError:
        print("⏱️ No speech detected. Try again.")

print("🔊 Listening...")
try:
    # Convert speech to text
    user_input = recognizer.recognize_google(audio)
    print(f"🗣️ You said: {user_input}")

    # Send to Gemini
    response = model.generate_content(user_input)
    reply = response.text
    print(f"🤖 Gemini says: {reply}")

    # Speak the response
    tts.say(reply)
    tts.runAndWait()

except sr.UnknownValueError:
    print("❌ Could not understand audio.")
except sr.RequestError as e:
    print(f"⚠️ STT error: {e}")
except Exception as e:
    print(f"⚠️ Error: {e}")
finally:
    tts.stop()
