import pyttsx3 as p3
import speech_recognition as sr
import webbrowser
import datetime as dt
import pyjokes as pj
import time


#this is speech to text function
def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:   #to catch voice
        print("LISTENING...")           #indicates that it has started listening
        recognizer.adjust_for_ambient_noise(source)#noice cancellation
        audio = recognizer.listen(source)
        #for recognizing the the voice if not recognized...it follows the exception
        try:
            print("Recognizing....")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Nahi samajh paya bhai...")

#text to speech
def txspeech(x):
    engine = p3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id) #male female voices 0=male 1=female
    rate=engine.getProperty('rate')
    engine.setProperty('rate',150)#speed rate
    engine.say(x)
    engine.runAndWait()


if __name__=="__main__":

    if "listen" in sptext().lower():


    # if sptext().lower() == "hey bro":
        while True:
        # bro is the name of ai..it will respond when we call him
            data1=sptext().lower()
            if "your name" in data1:  #takes data1 as input
                name="my name is bro"
                txspeech(name)

            elif "who created you" in data1:
                creator="atharva is my creator"
                txspeech(creator)

            elif "google" in data1:
                webbrowser.open("https://www.google.com/")

            elif "youtube" in data1:
                webbrowser.open("https://www.youtube.com/")

            elif "profile" in data1:
                webbrowser.open("https://github.com/AthrNAIK?tab=repositories")

            elif "joke" or "laugh" in data1:
                joke_1=pj.get_joke(language="en",category="neutral")
                txspeech(joke_1)

            elif 'play song' or 'music' in data1:
                pass

        # elif "time" in data1:
        #   time=dt.datetime.now().strftime("%I%M%P")
        #   txspeech(time)

            elif 'exit' or 'bahar' in data1:
                sptext("Thankyou Bhai")
                break

            else :
                sptext("Nahi Samjha")

            time.sleep(5)


    else:
        print("Thanks")


# note: THIS CODE IS STILL IN DEVELOPMENT IT GIVES UNEXPECTED OUTPUTS
