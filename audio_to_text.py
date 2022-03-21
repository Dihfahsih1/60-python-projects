# importing libraries 
import speech_recognition as sr 

# create a speech recognition object
r = sr.Recognizer()
def startConvertion(lang = 'en-IN'):
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        try:
            print('start speaking')
            audio_data = r.record(source, duration=10) #stop receiving input after 10 seconds
            print("converting...")
            # convert speech to text
            text = r.recognize_google(audio_data, language=lang)
            print(text)
        except:
            print("can not connect to the internet")
startConvertion()