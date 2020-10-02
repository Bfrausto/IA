import random

vReglas= []
valores= []
auxValores= []
regla=0
def setup():
    size(1000,1000)
def checar(eden,reglas,bordes):
    aleatorio() if eden==1 else unitario()
    borde= 0 if bordes==1 else 1 if bordes==2 else 2  #0=periodico 1=reflejante 2=absorbente
    deterministica(borde) if reglas==1 else wolfram(borde)
    
      
   

#def vcv():
#    print('hola')
#def cv():
#    print('hola')

def unitario():
    valores=[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]
        
def aleatorio():
    for a in range(21):
        valores.append(random.randint(0, 1))
        #print(valores[a])


def wolfram(borde):
    regla=input("Ingresa el numero de la regla a utilizar: ")
    regla=bin(regla)
    for a in range(2,len(regla)):
        vReglas.append(a)
       # print(regla[a])
    print(v)
    for i in range(len(valores)):
        vi=0
        c=valores[i]
        vd=0
        if i==0:
            vi=0 if bordes==0 else valores[len(valores)] if bordes==1 else c  
        elif i==len(valores):
            vi=0 if bordes==0 else valores[0] if bordes==1 else c
        if vi==0 and c==0 and vd==0:
            auxValores.append(vReglas[0])
        elif vi==0 and c==0 and vd==1:
            auxValores.append(vReglas[1])
        elif vi==0 and c==1 and vd==0:
            auxValores.append(vReglas[2])
        elif vi==0 and c==1 and vd==1:
            auxValores.append(vReglas[3])
        elif vi==1 and c==0 and vd==0:
            auxValores.append(vReglas[4])
        elif vi==1 and c==0 and vd==1:
            auxValores.append(vReglas[5])
        elif vi==1 and c==1 and vd==0:
            auxValores.append(vReglas[6])
        else:
            auxValores.append(vReglas[7])   
       
    valores=auxValores
    for b in valores:
        print b,  


def deterministica(borde):    
    vReglas.append(input("Ingresa el valor correspondiente a (0,0): "))
    vReglas.append(input("Ingresa el valor correspondiente a (0,1): "))
    vReglas.append(input("Ingresa el valor correspondiente a (1,0): "))
    vReglas.append(input("Ingresa el valor correspondiente a (1,1): "))
    #for b in vReglas:
    #    print(b)


    
eden=input('Ingresa el eden: Aleatorio(1) o Unitario(2): ')
#vecinos=input("Ingresa el rango de vecinos: CV(1) o VCV(2) : ")
reglas= input("Ingresa el rango de vecinos: Determinitica{VC}(1) o wolfram{VCV}(2) :")
bordes= input("Ingrese el tipo de borde: Absorbente(1), Periodicos(2) o Reflejantes(3) : ")
checar(eden,reglas,bordes)

# reglas



def draw(): 
    rect(20,10,50,50)
    rect(70,10,50,50)
    rect(x,y,50,50)






