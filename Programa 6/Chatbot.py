from nltk.chat.util import Chat, reflections
pares = [

    [
        r"(.*) programación",
        ["he leido sobre el tema ","Me parece algo interesante"]
    ],

    [
        r"mi nombre es (.*)",
        ["Hola , como estas ?",]
    ],
    [
        r"cuál es tu nombre ?",
        ["Mi nombre es Chatbot ",]
    ],
    [
        r"cómo te llamas ?",
        ["Mi nombre es Chatbot ",]
    ],
    [
        r"cómo estás ?",
        ["Bien, y tu?","He estado mejor, y tu?"]
    ],
    [
        r"disculpa",
        ["No pasa nada",]
    ],
    [
        r"hola ?|hey|buenas|que tal",
        ["Hola", "Que tal","Hola, mucho gusto"]
    ],
        [
        r"(.*)sabes hacer ?",
        ["no mucho, soy muy principiante","estoy aprendiendo a conversar con personas"]
    ],
        [ 
        r"(.*) gusta hacer ?",
        ["conocer personas y saber de ellas","me gusta hablar contigo",]
    ],
    [
        r"qué (.*) quieres ?",
        ["Nada, gracias",]

    ],
    [
        r"(.*) creado ?",
        ["Fui creado hoy por Fernanda y Brian",]
    ],

    [
        r"me voy|finalizar|bye|chao|nos vemos",
        ["Chao","Fue bueno hablar contigo",]
        
    ],
        [
        r"qué edad tienes|cuántos años tienes",
        ["La edad es relativa","creo que aun no cumplo ni un año", "no me gusta decir mi edad"]
        
    ],
        [
        r"me caes bien",
        ["Tu tambien eres genial","igual tu a mi"]
        
    ],
        [
        r"(.*) bien gracias",
        ["Me alegro mucho","es bueno saber eso"]
        
    ],
           [
        r"(.*) ser mi amiga ?",
        ["Eso seria fantastico","me agrada mucho esa idea","Claro, serás mi primer amigo"]
        
    ],
    [
        r"adiós ?",
        ["Nos vemos","Hasta luego",]
    ],

]

def chatear():
    mis_reflexions = {
}
    #print("Hola soy un bot") #mensaje por defecto
    chat = Chat(pares, mis_reflexions)
    chat.converse()
chatear()
