import pyttsx3  as txt
import speech_recognition as sr
import webbrowser as wb
import datetime as dt
import pyjokes as pj 

#speech recognizer takes input and returns the answer
def sptext():
  recognizer = sr.Recognizer()
  with sr.Microphone() as source:
    print('Listening...')
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listn(source)
    try :
      print('recognizing')
      data = recognizer.recognize_google(audio)
      print(data)

    except sr.UnknownValueError:
      print('not understanding')
      