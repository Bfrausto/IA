import random

vReglas= []

regla=0
def deterministica(borde):    
    vReglas.append(input("Ingresa el valor correspondiente a (0,0): "))
    vReglas.append(input("Ingresa el valor correspondiente a (0,1): "))
    vReglas.append(input("Ingresa el valor correspondiente a (1,0): "))
    vReglas.append(input("Ingresa el valor correspondiente a (1,1): "))
    #for b in vReglas:
    #    print(b)


def checar(eden,reglas,bordes,generaciones):

    if eden==1:
        valores= aleatorio()
    else:
        valores=unitario()


    borde= 0 if bordes==1 else 1 if bordes==2 else 2  #0=periodico 1=reflejante 2=absorbente
    deterministica(borde) if reglas==1 else wolfram(borde,valores,generaciones)
    
      
   

#def vcv():
#    print('hola')
#def cv():
#    print('hola')

def unitario():
    print(' hola')
    valores=[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]
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
    reglas=[]
    print(regla)
    print(len(regla))
    regla.replace("b","0")#############################tenemos que arreglar la conversión a binario
    print(regla)
    print("0,0,0-> ",regla[2])
    print("0,0,1-> ",regla[3])
    print("0,1,0-> ",regla[4])
    print("0,1,1-> ",regla[5])
    print("1,0,0-> ",regla[6])
    print("1,0,1-> ",regla[7])
    print("1,1,0-> ",regla[8])
    print("1,1,1-> ",regla[9])
    vi=0
    vd=0
    auxValores=[]
    for x in range(generaciones):
        for i in range(len(valores)):
            c=valores[i]
            print(i)
            if i==0:
                vi=0 if bordes==0 else valores[len(valores)] if bordes==1 else c  
                vd=valores[i+1]
            elif i==len(valores)-1:
                vd=0 if bordes==0 else valores[0] if bordes==1 else c
                vi=valores[i]
            else:
                vi=valores[i-1] 
                vd=valores[i+1]    
            if vi==0 and c==0 and vd==0:
                auxValores.insert(i,regla[2])
            elif vi==0 and c==0 and vd==1:
                auxValores.insert(i,regla[3])
            elif vi==0 and c==1 and vd==0:
                auxValores.insert(i,regla[4])
            elif vi==0 and c==1 and vd==1:
                auxValores.insert(i,regla[5])
            elif vi==1 and c==0 and vd==0:
                auxValores.insert(i,regla[6])
            elif vi==1 and c==0 and vd==1:
                auxValores.insert(i,regla[7])
            elif vi==1 and c==1 and vd==0:
                auxValores.insert(i,regla[8])
            else:
                auxValores.insert(i,regla[9])  
        valores=auxValores
        print(' '.join(map(str, auxValores)))
        
        
        



    
eden=int(input('Ingresa el eden: Aleatorio(1) o Unitario(2): '))
#vecinos=input("Ingresa el rango de vecinos: CV(1) o VCV(2) : ")
reglas= int(input("Ingresa el rango de vecinos: Determinitica{VC}(1) o wolfram{VCV}(2) :"))
bordes= int(input("Ingrese el tipo de borde: Absorbente(1), Periodicos(2) o Reflejantes(3) : "))
generaciones= int(input("Ingrese el # generaciones: "))
checar(eden,reglas,bordes,generaciones)

# reglas

