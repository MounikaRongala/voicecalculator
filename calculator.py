import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak output
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech and convert to text
def get_voice_input():
    with sr.Microphone() as source:
        print("🎤 Listening... Speak your calculation:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("🧠 Recognizing...")
        expression = recognizer.recognize_google(audio)
        print(f"You said: {expression}")
        return expression
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand that.")
        return None
    except sr.RequestError:
        speak("Sorry, the speech service is unavailable.")
        return None

# Function to evaluate and speak the result
def calculate_expression(expression):
    try:
        result = eval(expression)
        print(f"🧮 Result: {result}")
        speak(f"The result is {result}")
    except:
        speak("Sorry, I couldn't calculate that.")

# Main program loop
def main():
    speak("Welcome to the voice calculator. Say your math expression.")
    while True:
        expression = get_voice_input()
        if expression:
            if "exit" in expression or "stop" in expression:
                speak("Goodbye!")
                break
            calculate_expression(expression)

if __name__ == "__main__":
    main()
