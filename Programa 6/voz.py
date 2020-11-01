import pyttsx
engine = pyttsx.init()
voices = engine.getProperty('voices')
for voice in voices:
    engine.setProperty('voice', voice.id)
    engine.say('Hola Carlos Julio, bienvenido a Vive digital')
    print (voice.id)
engine.runAndWait()