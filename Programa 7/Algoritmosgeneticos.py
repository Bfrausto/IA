import random
import pandas
from pandas import DataFrame
import matplotlib.pyplot as plt

salidas = open("salida.txt", "w")
def leer():
    archivo = open("entrada.txt", "r")
    entrada = archivo.read()
    cont,r,g,m=0,0,0,0
    for ver in entrada.split(","):
        ver = ver.rstrip()
        if cont==0:
            r=int(ver)
        elif cont==1:
            g=int(ver)
        else:
            m=int(ver)
        cont+=1
    return r, g, m

def crear(rango):
    individuos=[]
    for x in range(rango):
        individuos.append(random.randint(-255, 255))
        #print(x)
    return individuos
    
def ruleta(individuos,generacion,rango):
    for numGen in range(generacion):
        sFit=0
        funcFit=[]
        pS=[]
        data=[]
        nums=[]
        copia=[]
        for i in individuos:
            aux=funcionRuleta(i)#evalua x en la funcion fitness
            funcFit.append(aux)
            sFit+=(aux)

        print(sFit)
        # print("")
        for i in funcFit:#realiza ps(i)
            aux2=i/sFit*100
            pS.append(aux2) 
        #print(' '.join(map(str, pS)))
        for i in range(1,len(individuos)+1):#obtine los i de los datos
            nums.append(i)

        for x in range(len(individuos)):#agrega los datos de la tabla a data
            data.append([individuos[x],funcionRuleta(individuos[x]),funcFit[x],pS[x]])

        headers=[ "x", "f(x)","fitness", "ps(i)"]
        salidas.write("Generacion numero : "+str(numGen)+"\n")
        salidas.write(pandas.DataFrame(data, nums,headers).to_string())
        salidas.write("\n----------------------------------\n\n")

        print(pandas.DataFrame(data, nums,headers))#realiza la tabla
        for x in range(len(individuos)):# se eliminan los datos <0.25
           if pS[x]>=0.25:
                copia.append(individuos[x])
        individuos=copia
        copia=[]
        if numGen==generacion-1:#realiza la grafica
            datos = {'i':nums,
                'ps(i)':pS}
            df = DataFrame(datos,columns=['i','ps(i)'])
            df.plot(x ='i', y='ps(i)', kind = 'line')
            plt.show()
            

def funcionRuleta(x):
    x=(2*(x*x))-x+1
    return x

def torneo(individuos,generacion):
    print ("hola")

def crucecs(individuos,generacion):
    print ("hola")


def crucess(individuos,generacion):
    print ("hola")
rango, generacion, metodo= leer()
individuos=crear(rango)
ruleta(individuos,generacion,rango) if metodo ==0 else torneo(individuos,generacion) if metodo ==1 else crucecs(individuos,generacion) if metodo ==2 else crucess(individuos,generacion)

#print(' '.join(map(str, individuos)))
# from pandas import DataFrame
# import matplotlib.pyplot as plt
   
# Data = {'Year': [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010],
#         'Unemployment_Rate': [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
#        }
  
# df = DataFrame(Data,columns=['Year','Unemployment_Rate'])
# df.plot(x ='Year', y='Unemployment_Rate', kind = 'line')
# plt.show()

# regla = bin(regla)
#     reglas = ""
#     for a in range(0, 10-len(regla)):
#         reglas += '0'
#     for x in range(2, len(regla)):
#         reglas += regla[x]
