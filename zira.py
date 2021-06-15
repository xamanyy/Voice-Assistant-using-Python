import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser
import os

browser_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe %s"
webbrowser.register('brave', None, webbrowser.BackgroundBrowser(browser_path))


# webbrowser.register('brave', None)

#Taking Voce access from Microsoft
engine = pyttsx3.init('sapi5')

#Store the Voice from Windows
voices = engine.getProperty('voices')
# print(voices[1].id)

#Set the female voice (Zira)
engine.setProperty('voice',voices[1].id)


#Speak Function
def speak(audio):
  engine.say(audio)
  engine.runAndWait()

#welcome Function
def welcome():
  hour = int(datetime.datetime.now().hour)
  if(hour>=0 and hour<12):
    speak("Good Morning Sir")
  elif(hour>=12 and hour<18):
    speak("Good Afternoon Sir")
  else:
    speak("Good Evening Sir")
  speak("Zira Here What help You need")

#To take speech of Userand convert it into String
def takeCommand():
  record = sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening..")
    record.pause_threshold = 0.5
    audio = record.listen(source)
  try:
    print("Recoznizing")
    query= record.recognize_google(audio,language='en-in')
    print("User said:" + query)
  except Exception as e:
    # print(e)
    print("Say Again")
    return "None"
  return query

#Main Function
if __name__ == '__main__':
  welcome()
  while True:
  # if 1:
    query = takeCommand().lower()

    if 'wikipedia' in query:
      speak("Searching wikipedia")
      query = query.replace("wikipedia","")
      result =wikipedia.summary(query , sentences = 2)
      print(result)
      speak("Searching wikipedia")
      speak(result)
      speak("Thank you Sir")
    elif 'open youtube' in query:
      webbrowser.get('brave').open_new_tab('youtube.com')
    elif 'open google' in query:
      webbrowser.get('brave').open_new_tab('google.com')
    elif 'open coinmarket' in query:
      webbrowser.get('brave').open_new_tab('coinmarket.com')
    elif 'open linkedin' in query:
      webbrowser.get('brave').open_new_tab('linkedin.com')

    elif 'time' in query:
      time = datetime.datetime.now().strftime("%H:%M:%S")
      speak(f"Sir the time is {time}")
    elif 'open android' in query:
      codePath = "C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
      os.startfile(codePath)
    elif 'open code' in query:
      codeArea = "C:\\Users\\Lenovo\\AppData\\Local\Programs\\Microsoft VS Code\\Code.exe"
      os.startfile(codeArea)
    elif 'open brave' in query:
      codeSpace = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
      os.startfile(codeSpace)
    elif 'open ui' in query:
      codeList = "C:\\Users\\Lenovo\\AppData\\Local\\UiPath\\UiPath.Studio.exe"
      os.startfile(codeList)
    elif 'close' in query:
      exit()


      

