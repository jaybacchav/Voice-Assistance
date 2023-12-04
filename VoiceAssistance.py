import speech_recognition as sr
import pyttsx3

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to the user's voice
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio)  # Recognize speech using Google Speech Recognition
            print(f"User said: {command}")
            return command
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            return ""
        except sr.RequestError as e:
            print(f"Error: {e}")
            return ""

# Function to process user commands
def process_command(command):
    if "hello" in command.lower():
        speak("Hello there!")
    elif "how are you" in command.lower():
        speak("I'm doing well, thank you!")
    elif "goodbye" in command.lower():
        speak("Goodbye!")
        exit()
    else:
        speak("I'm not sure how to respond to that.")

# Main loop for the voice assistant
while True:
    command = listen()
    if command:
        process_command(command)
