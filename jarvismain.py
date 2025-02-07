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
    audio = recognizer.listen(source)
    try :
      print('recognizing')
      data = recognizer.recognize_google(audio)
      print(data)
      return data

    except sr.UnknownValueError:
      print('not understanding')
      

    

def speechtotext(x):
  engine = txt.init()
  voices = engine.getProperty('voices')
  engine.setProperty('voice',voices[0].id)
  rate = engine.getProperty('rate')
  engine.setProperty('rate',200)
  engine.say(x)
  engine.runAndWait()

#speechtotext("hi,i am jarvis, your personal voice assistant, how may i help you sir?")





if __name__ == '__main__':
  
  #if sptext().lower() == "hey peter":
      data1 = sptext().lower() 
      if "your name" in data1:
         name="my name is peter"
         speechtotext(name)
      
  #else:
   # print('thanks')