#creating a assistance like siri for pc named kiwi
import pyttsx3 #text-to-speech conversion
import datetime
import speech_recognition as sr

#for the task
import wikipedia
import webbrowser
import os
#import pyaudio 



engine = pyttsx3.init('sapi5')   #sapi5 provided by microsoft to speech conversion
voices = engine.getProperty('voices')  #taking the voices property from python

#printing the voices , python voices[0] gives the voice of a male and 1 gives female

engine.setProperty('voice' , voices[1].id)




#the built in function to store the info for kiwi to speak
def speak(audio):    
    engine.say(audio)
    engine.runAndWait()

#the built in function to greet according to the time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning')

    elif hour>=12 and hour<18:
        speak('Good Afternoon')

    else:
        speak('Good evening')

    speak('My name is Kiwi, how may I help?')

#the built in funcation to take the input from user
def takeCommand():
    r = sr.Recognizer()       #syntax for the recognization of speech
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1   #second to take gap while speaking
        audio = r.listen(source)

    try: 
        print("Recognizing...")
        query = r.recognize_google(audio , language='en-in')   #the language to understand
        print(f"User said : {query} \n")

    except Exception as e:   #if the pc couldn't recognize
        #print(e)

        print("Couldn't recognize. Say it again please")
        return "NONE"
    return query




if __name__ == "__main__":
    wishMe()
    if 1:
        query= takeCommand().lower()
 
        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query , sentences =  2) #returns 2 sentences from wikipedia
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open movies' in query:
            MOVIEEEEE = "D:\\MOVIEEEEE"
            movies = os.listdir(MOVIEEEEE)
            print(movies)
            os.startfile(os.path.join( MOVIEEEEE, movies[0] ))

        elif 'time right now' in query:
            try: 
             startTime = datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"The time is{startTime}")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to recognize")


            


        

