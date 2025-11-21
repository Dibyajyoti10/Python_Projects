  #THE OG CODE

# import speech_recognition as speech
# import webbrowser as web
# import pyttsx3 

# recognizer = speech.Recognizer()
# engine = pyttsx3.init()

# # Get the available voices
# voices = engine.getProperty('voices')

# # Set the voice (e.g., the second voice in the list)
# engine.setProperty('voice', voices[1].id)

# # Speak the text
# def speak (text):
#     engine.say(text)
#     engine.runAndWait()
# # print number of voices available in pyttsx3 ---> 2
# # print("Number of available voices:", len(voices))
# def processCommand(c):
#     if  "friday" in c.lower():
#         speak("Yes Boss")
#     elif "open google" in c.lower():
#         speak("Opening Google")
#         web.open("https://www.google.com")
#     elif "open youtube" in c.lower():
#         web.open("https://www.youtube.com")
    



# if __name__ == "__main__":
#     speak("Setting up the System!!")
#     speak("Initializing Friday....")
#     speak("Hello BOSS")
    
#     while True:
#         r = speech.Recognizer()
#         print("Recognizing....")
#         try:
#             with speech.Microphone() as source:
#                 print("What's the order BOSS")
#                 recognizer.adjust_for_ambient_noise(source)
#                 audio = r.listen(source, timeout=2, phrase_time_limit=1)
#             word = r.recognize_google(audio)
#             if(word.lower() == "friday"):
#                 speak("Ya")
#                 with speech.Microphone() as source:
#                     print("Initialised friday")
#                     audio = r.listen(source)
#                     command = r.recognize_google(audio)

#                 processCommand(command)  
#         except Exception as e:
#             print("Some malfunctioning is occuring; {0}".format(e))




# #THE MODIFIED CODE   
# import speech_recognition as speech
# import webbrowser as web
# import pyttsx3

# recognizer = speech.Recognizer()
# engine = pyttsx3.init()

# # Get the available voices
# voices = engine.getProperty('voices')

# # Set the voice (e.g., the second voice in the list)
# engine.setProperty('voice', voices[1].id)

# # Speak the text
# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# def processCommand(c):
#     if "friday" in c.lower():
#         speak("Yes Boss")
#     elif "open google" in c.lower():
#         speak("Opening Google")
#         web.open("https://www.google.com")
#     elif "open youtube" in c.lower():
#         speak("Opening YouTube")
#         web.open("https://www.youtube.com")

# if __name__ == "__main__":
#     speak("Setting up the System!")
#     speak("Initializing Friday...")
#     speak("Hello BOSS")

#     while True:
#         print("Recognizing....")
#         try:
#             with speech.Microphone() as source:
#                 print("What's the order BOSS")
#                 recognizer.adjust_for_ambient_noise(source)
#                 audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)  # Increased limits
#             word = recognizer.recognize_google(audio)
#             print(f"You said: {word}")
#             if "friday" in word.lower():
#                 speak("Yes Boss")
#             #here i am
#             elif "shut down" in word.lower():
#                 speak("Shutting down the system")
#                 with speech.Microphone() as source:
#                     print("Awaiting command...")
#                     audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)  # Increased limits
#                     command = recognizer.recognize_google(audio)
#                     print(f"Command: {command}")
#                 processCommand(command)
#         except speech.UnknownValueError:
#             print("Sorry, I didn't catch that.")
#             speak("Sorry, I didn't catch that.")
#         except speech.RequestError as e:
#             print(f"Could not request results from Google Speech Recognition service; {e}")
#             speak("I'm having trouble with the connection.")
#         except Exception as e:
#             print(f"Some malfunction is occurring: {e}")




#THE MODIFIED CODE 2.0
import speech_recognition as speech
import webbrowser as web
import pyttsx3

recognizer = speech.Recognizer()
engine = pyttsx3.init()

# Get the available voices
voices = engine.getProperty('voices')

# Set the voice (e.g., the second voice in the list)
engine.setProperty('voice', voices[1].id)

# Speak the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "friday" in c.lower():
        speak("Yes Boss")
    elif "open google" in c.lower():
        speak("Opening Google")
        web.open("https://www.google.com")
    elif "open youtube" in c.lower():
        speak("Opening YouTube")
        web.open("https://www.youtube.com")
    elif "open whatsapp" in c.lower():
        speak("Opening Whatsapp")
        web.open("https://www.whatsapp.com")
    elif "open linkedin" in c.lower():
        speak("Opening Linkedin")
        web.open("https://www.linkedin.com/in/dibyajyoti-rautaray-4556902b6")
    elif "open git" in c.lower():
        speak("opening github")
        web.open("https://github.com/Dibyajyoti10")

if __name__ == "__main__":
    speak("Setting up the System!")
    print("Setting up the System!")
    speak("Initializing Friday...")
    print("Initializing Friday...")
    speak("Hello BOSS")
    print("Hello BOSS")


    while True:
        print("Recognizing....")
        try:
            with speech.Microphone() as source:
                print("What's the order BOSS")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)  # Increased limits
            word = recognizer.recognize_google(audio)
            print(f"You said: {word}")
            if "friday" in word.lower():
                speak("Yes Boss")
            #here i am
            elif "shut down" in word.lower():
                speak("Shutting down the system")
                with speech.Microphone() as source:
                    print("Awaiting command...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)  # Increased limits
                    command = recognizer.recognize_google(audio)
                    print(f"Command: {command}")
                processCommand(command)
        except speech.UnknownValueError:
            print("Sorry, I didn't catch that.")
            speak("Sorry, I didn't catch that.")
        except speech.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            speak("I'm having trouble with the connection.")
        except Exception as e:
            print(f"Some malfunction is occurring: {e}")
