from nltk.chat.util import Chat, reflections
pares = [

        [
        r"(.) programacion",
        ["programacion ? o_O",]
    ],

    [
        r"mi nombre es (.)",
        ["Hola %1, como estas ?",]
    ],
     [
        r"cual es tu nombre ?",
        ["Mi nombre es Chatbot ?",]
    ],
    [
        r"como estas ?",
        ["Bien, y tu?",]
    ],
    [
        r"disculpa (.)",
        ["No pasa nada",]
    ],
    [
        r"hola|hey|buenas",
        ["Hola", "Que tal",]
    ],
    [
        r"que (.) quieres ?",
        ["Nada gracias",]

    ],
    [
        r"(.*) creado ?",
        ["Fui creado hoy",]
    ],

    [
        r"me voy|finalizar",
        ["Chao","Fue bueno hablar contigo",]
        
    ],
    [
        r"quit ?",
        ["Nos vemos","Hasta luego",]
    ],

]

def chatear():
    mis_reflexions = {
}
    print("Hola soy un bot") #mensaje por defecto
    chat = Chat(pares, mis_reflexions)
    chat.converse()
chatear()
