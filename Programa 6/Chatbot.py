from nltk.chat.util import Chat, reflections
pares = [

        [
        r"(.*) programacion",
        ["programacion ? o_O",]
    ],

    [
        r"mi nombre es (.*)",
        ["Hola , como estas ?",]
    ],
     [
        r"cual es tu nombre ?",
        ["Mi nombre es Chatbot ?",]
    ],
    [
        r"como estas ?",
        ["Bien, y tu?","He estado mejor, y tu?"]
    ],
    [
        r"disculpa (.*)",
        ["No pasa nada",]
    ],
    [
        r"hola|hey|buenas",
        ["Hola", "Que tal",]
    ],
        [
        r"(.*)puedes hacer ?",
        ["no mucho, soy un principiante","estoy aprendiendo a conversar con personas"]
    ],
        [
        r"(.*) gusta hacer ?",
        ["conocer personas y saber de ellas","me gusta hablar contigo",]
    ],
    [
        r"que (.*) quieres ?",
        ["Nada gracias",]

    ],
    [
        r"(.*) creado ?",
        ["Fui creado hoy por Fernanda y Brian",]
    ],

    [
        r"me voy|finalizar|bye|chao",
        ["Chao","Fue bueno hablar contigo",]
        
    ],
        [
        r"que edad tienes|cuantos años tienes",
        ["La edad es relativa","Mmmm creo que aun no cumplo un año"]
        
    ],
        [
        r"me caes bien",
        ["Wow, gracias","igual tu a mi"]
        
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
