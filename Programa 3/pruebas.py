import random

vReglas= []

regla=0
def deterministica(borde,valores,generaciones):    
    vReglas.append(input("Ingresa el valor correspondiente a (0,0): "))
    vReglas.append(input("Ingresa el valor correspondiente a (0,1): "))
    vReglas.append(input("Ingresa el valor correspondiente a (1,0): "))
    vReglas.append(input("Ingresa el valor correspondiente a (1,1): "))
    auxValores=[]
    for x in range(generaciones):
        print(' '.join(map(str, valores)))
        for i in range(len(valores)):
            c=valores[i]
            if i==len(valores)-1:
                v=0 if borde==0 else valores[0] if borde==1 else c
            else:
                v=valores[i+1]     
            print(c,v)
            if c==0 and v==0 :
                auxValores.insert(i,int(vReglas[0]))
            elif c==0 and  v==1:
                auxValores.insert(i,int(vReglas[1]))
            elif c==1 and v==0 :
                auxValores.insert(i,int(vReglas[2]))
            else:
                auxValores.insert(i,int(vReglas[3]))       
        valores=auxValores
        auxValores=[]
    #for b in vReglas:
    #    print(b)


def checar(eden,reglas,bordes,generaciones):

    if eden==1:
        valores= aleatorio()
    else:
        valores=unitario()
    borde= 0 if bordes==1 else 1 if bordes==2 else 2  #0=periodico 1=reflejante 2=absorbente
    deterministica(borde,valores,generaciones) if reglas==1 else wolfram(borde,valores,generaciones)
    
      
   

#def vcv():
#    print('hola')
#def cv():
#    print('hola')

def unitario():
    valores=[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]
     #valores=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    return valores
def aleatorio():
    valores= []
    for a in range(21):
        valores.append(random.randint(0, 1))
        #print(valores[a])
    
    print(' '.join(map(str, valores)))
    return valores

def wolfram(borde,valores,generaciones):
    regla=int(input("Ingresa el numero de la regla a utilizar: "))
    regla=bin(regla)
    reglas=""
    for a in range(0,10-len(regla)):
        reglas+='0'
    for x in range(2,len(regla)):
        reglas+=regla[x]
    print(reglas)     
    print("0,0,0-> ",reglas[0])
    print("0,0,1-> ",reglas[1])
    print("0,1,0-> ",reglas[2])
    print("0,1,1-> ",reglas[3])
    print("1,0,0-> ",reglas[4])
    print("1,0,1-> ",reglas[5])
    print("1,1,0-> ",reglas[6])
    print("1,1,1-> ",reglas[7])
    vi=0
    vd=0
    auxValores=[]
    auxG=[]
    for x in range(generaciones):
        #print(' '.join(map(str, valores)))
        for a in valores:
            if a == 1:
                auxG.append('■')
            else:
                auxG.append(' ')
        print(' '.join(map(str, auxG)))
        auxG=[]
        for i in range(len(valores)):
            c=valores[i]
            if i==0:
                vi=0 if borde==0 else valores[len(valores)-1] if borde==1 else c  
                vd=valores[i+1]
            elif i==len(valores)-1:
                vd=0 if borde==0 else valores[0] if borde==1 else c
                vi=valores[i-1]
            else:
                vi=valores[i-1] 
                vd=valores[i+1]    
            if vi==0 and c==0 and vd==0:
                auxValores.insert(i,int(reglas[0]))
            elif vi==0 and c==0 and vd==1:
                auxValores.insert(i,int(reglas[1]))
            elif vi==0 and c==1 and vd==0:
                auxValores.insert(i,int(reglas[2]))
            elif vi==0 and c==1 and vd==1:
                auxValores.insert(i,int(reglas[3]))
            elif vi==1 and c==0 and vd==0:
                auxValores.insert(i,int(reglas[4]))
            elif vi==1 and c==0 and vd==1:
                auxValores.insert(i,int(reglas[5]))
            elif vi==1 and c==1 and vd==0:
                auxValores.insert(i,int(reglas[6]))
            else:
                auxValores.insert(i,int(reglas[7]))       
        valores=auxValores
        auxValores=[]
        

            
        
        
        



    
eden=int(input('Ingresa el eden: Aleatorio(1) o Unitario(2): '))
#vecinos=input("Ingresa el rango de vecinos: CV(1) o VCV(2) : ")
reglas= int(input("Ingresa el rango de vecinos: Deterministica{CV}(1) o wolfram{VCV}(2) :"))
bordes= int(input("Ingrese el tipo de borde: Absorbente(1), Periodicos(2) o Reflejantes(3) : "))
generaciones= int(input("Ingrese el # generaciones: "))
checar(eden,reglas,bordes,generaciones)

# reglas

