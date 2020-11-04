

print("Conectado")
recognizer = sr.Recognizer()


while True:
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    linea = recognizer.recognize_google(audio,language="es-MX")
    
    linea = linea.lower()
    linea = normalize(linea)
    inp = linea

    print(linea)

    salida = inp.encode("UTF8")
    
    if inp == "exit":
        break

print("Terminado")
