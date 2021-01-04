import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyjokes


# giving the assistant, his voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


# selecting google chrome as the default browser
chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))


# what the assistant will say
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# the assistant's first encounter with the user
def greetings():
    hour = int(datetime.datetime.now().hour)

    if (hour >= 0) and (hour < 12):
        speak("Good Morning, sir!")

    elif (hour >= 12) and (hour < 18):
        speak("Good afternoon, sir!")

    else:
        speak("Good evening, sir!")

    speak("Tell me, how can I help you?")


# assistant will take commands by the user
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing.....')
        query = r.recognize_google(audio, language='en-in')
        print(f"You said : {query}\n")

    except Exception as e:
        print('Say that again please...')
        return 'None'
    return query


# assistant will greet the user
greetings()


# main commands
while True:
    query = take_command().lower()

    if 'how are you' in query:
        speak("I am fine, thank you for asking sir")

    elif 'wikipedia' in query:
        speak('Searches Wikipedia.....')
        query = query.replace('wikipedia','')
        results = wikipedia.summary(query,sentences=2)
        print(results)

    elif 'open youtube' in query:
        webbrowser.get("chrome").open_new_tab("youtube.com")

    elif 'open google' in query:
        webbrowser.get("chrome").open_new_tab('google.com')

    elif 'open instagram' in query:
        webbrowser.get("chrome").open_new_tab('instagram.com')

    elif 'open whatsapp web' in query:
        webbrowser.get("chrome").open_new_tab('web.whatsapp.com')
    
    elif 'open gmail' in query:
        webbrowser.get("chrome").open_new_tab('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')

    elif 'the time' in query:
        speak(f'the time is {datetime.datetime.now().strftime("%H:%M:%S")}')

    elif 'open vs code' in query:
        code_path = "C:\\Users\\HP\\Microsoft VS Code\\Code.exe"
        os.startfile(code_path)

    elif 'open pycharm' in query:
        os.startfile("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.2\\bin\\pycharm64.exe")

    elif 'a joke' in query:
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)

    elif ('quit' in query) or ('exit' in query) or ('bye bye' in query):
        break


