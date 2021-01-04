from gtts import gTTS

with open('sample_text','r') as text:
    audio = text.read()
    print('converting the text to WAV file..........')

    try:
        audio_file = gTTS(audio,lang='en')
        audio_file.save('text_to_speech.wav')
    except:
        print('Problem Occured')

