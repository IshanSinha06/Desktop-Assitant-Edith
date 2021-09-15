import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine=pyttsx3.init('sapi5')  #ye ek inbuilt voice dega
voice=engine.getProperty('voices') #This method is used to get the details with the help of this function.
engine.setProperty('voice', voice[1].id) #This method sets different properties of the model.

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    '''This function will make the speech audible in the system, 
    if you don't write this command then the speech will not be audible 
    to you.
    '''

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
    elif hour >=12 and hour < 16:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    
    speak("I am Edith, how may I  help you today?")

def takecommand():
    #it takes microphone input and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        r.pause_threshold = 1
        r.energy_threshold=50
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as Error:
        print("Please say that again.")
        return "None"
    
    return query

if __name__ == '__main__':
    wishMe()

    #Logic fo rexecuting tasks based on query
    while True:
        query=takecommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia..')
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open amazon' in query:
            webbrowser.open("amazon.in")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open leetcode' in query:
            webbrowser.open("leetcode.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open geek for geeks' in query:
            webbrowser.open("geekforgeeks.com")

        elif 'open code' in query:
            path='C:\\Users\\ishan\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk'
            os.startfile(path) 

         