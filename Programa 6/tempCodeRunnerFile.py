import pyttsx3
engine = pyttsx3.init()
while True:
    speech = input("Say Something : ")
    engine.say(speech)
    engine.runAndWait()
    if speech == 'exit':
        break