import speech_recognition as sr


speech = sr.Recognizer()

with sr.AudioFile('sample_speech.wav') as source:

    audio = speech.listen(source)

    print('converting audio to text.........')

    try :
        text = speech.recognize_google(audio)
        with open('speech_to_text.txt','w') as f:
            f.write(text)
            f.close()

    except :
        print('Problem occured.')
