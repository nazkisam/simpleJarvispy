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
      elif "old are you" in data1:
         age = "i am eighteen years old"
         speechtotext(age)
      elif 'now time' in data1:
         time = dt.datetime.now().strftime("%I%M%p")
         speechtotext(time)
      elif "youtube" in data1:
         wb.open("https://chatgpt.com/")
      elif "joke" in data1:
         jokes = pj.get_joke(language='en',category = 'netural')
         speechtotext(jokes)   


  #else:
   # print('thanks')