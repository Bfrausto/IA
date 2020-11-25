import random
import pandas
from pandas import DataFrame
import matplotlib.pyplot as plt

salidas = open("salida.txt", "w")


def leer():
    archivo = open("entrada.txt", "r")
    entrada = archivo.read()
    cont, r, g, m = 0, 0, 0, 0
    for ver in entrada.split(","):
        ver = ver.rstrip()
        if cont == 0:
            r = int(ver)
        elif cont == 1:
            g = int(ver)
        else:
            m = int(ver)
        cont += 1
    return r, g, m


def crear(rango):
    individuos = []
    for x in range(rango):
        individuos.append(random.randint(-255, 255))
        # print(x)
    return individuos


def ruleta(individuos, generacion, rango):
    max = []
    generaciones = []
    for i in range(1, generacion+1):  # obtine los i de los datos
        generaciones.append(i)
    for numGen in range(generacion):
        sFit = 0
        funcFit = []
        pS = []
        data = []
        nums = []
        copia = []
        numMax = 0
        for x in individuos:

            aux = funcionRuleta(x)  # evalua x en la funcion fitness
            funcFit.append(aux)
            sFit += (aux)
       # print(sFit)
        # print("")
        for i in funcFit:  # realiza ps(i)
            aux2 = i/sFit*100
            pS.append(aux2)
        #print(' '.join(map(str, pS)))
        for i in range(1, len(individuos)+1):  # obtine los i de los datos
            nums.append(i)

        # agrega los datos de la tabla a data y saca el maximo
        for x in range(len(individuos)):
            if funcionRuleta(individuos[x]) > numMax:
                numMax = funcionRuleta(individuos[x])
            data.append([individuos[x], funcionRuleta(
                individuos[x]), funcFit[x], pS[x]])
        max.append(numMax)
        headers = ["x", "f(x)", "fitness", "ps(i)"]
        salidas.write("Generacion numero : "+str(numGen)+"\n")
        salidas.write(pandas.DataFrame(data, nums, headers).to_string())
        elegirRandom(individuos) if generacion-1 != numGen else ""
        salidas.write("\n----------------------------------\n\n")

        # print(pandas.DataFrame(data, nums,headers))#realiza la tabla
        for x in range(len(individuos)):  # se eliminan los datos <0.25
            if pS[x] >= 0.25:
                copia.append(individuos[x])
        individuos = copia
        copia = []

        if numGen == generacion-1:  # realiza la grafica
            print(' '.join(map(str, max)))
            print(' '.join(map(str, generaciones)))
            datos = {'Generacion': generaciones, 'f(x)': max}
            df = DataFrame(datos, columns=['Generacion', 'f(x)'])
            df.plot(x='Generacion', y='f(x)', kind='line')
            plt.show()


def elegirRandom(individuos):
    numMut = random.randint(1, len(individuos))
    salidas.write("\n\nOcurrieron "+str(numMut)+" mutacion/es")
    for i in range(0, numMut):
        numero = random.randint(0, len(individuos)-1)
        individuos[numero] = mutacion(individuos[numero])


def funcionRuleta(x):
    x = (2*(x*x))-x+1
    return x


def torneo(individuos, generacion, rango):
    if len(individuos) % 2 == 0:
        ganadores = []
        data = []
        max = []
        numMax = 0
        generaciones = []
        cont = rango-1
        for i in range(1, generacion+1):  # obtine los i de los datos
            generaciones.append(i)
        for numGen in range(generacion):
            cont = rango-1
            nums = []
            data = []
            numMax = 0
            for x in range(int(rango/2)):
               # print(x)

                if funcionTorneo(individuos[x]) > funcionTorneo(individuos[cont]):
                    ganadores.append(individuos[x])
                    ganadores.append(individuos[x])
                else:
                    ganadores.append(individuos[cont])
                    ganadores.append(individuos[cont])
                cont -= 1
            # print(' '.join(map(str, individuos)))
            # print(' '.join(map(str, ganadores)))
            for i in range(1, len(individuos)+1):  # obtine los i de los datos
                nums.append(i)
            # agrega los datos de la tabla a data y saca el maximo
            for x in range(len(individuos)):
                if funcionTorneo(individuos[x]) > numMax:
                    numMax = funcionTorneo(individuos[x])
                data.append([individuos[x], funcionTorneo(individuos[x])])
            max.append(numMax)
            #print(' '.join(map(str, nums)))
            if individuos == ganadores:
                for i in range(2):
                    rand = random.randint(0, len(ganadores)-1)
                    ganadores[rand] = mutacion(ganadores[rand])

            headers = ["valor de x", "f(x)"]
            salidas.write("Generacion numero : "+str(numGen)+"\n")
            salidas.write(pandas.DataFrame(data, nums, headers).to_string())
            #elegirRandom(individuos) if generacion-1!= numGen else ""
            salidas.write("\n----------------------------------\n\n")

            individuos = ganadores
            ganadores = []

            if numGen == generacion-1:  # realiza la grafica
                datos = {'Generacion': generaciones, 'f(x)': max}
                df = DataFrame(datos, columns=['Generacion', 'f(x)'])
                df.plot(x='Generacion', y='f(x)', kind='line')
                plt.show()

    else:
        print("El numero de individuos ingresado no es correcto. \n(recuerda que deben ser pares)")


def funcionTorneo(x):
    x = (2*(x*x))+x-2
    return x


def mutacion(numero):
    numBind = bin(numero)
    mutacion, nuevoBin, mutado = "", "", 0
    numRandom = random.randint(1, 8)
    mutacion += "1" if numBind[0] == "-" else "0"
   
    for a in range(0, 10-len(numBind)):
        mutacion += '0'
    signo = 2 if mutacion[0] == "0" else 3
    for x in range(signo, len(numBind)):
        mutacion += numBind[x]

    numBin = mutacion
    for i in range(0, len(mutacion)):
        if i == numRandom:
            nuevoBin += "1" if mutacion[i] == "0" else "0"
        else:
            nuevoBin += mutacion[i]

    mutado = int(str(nuevoBin), 2)
    salidas.write("\n----------------------------------\n")

    salidas.write(str(numero)+" = "+numBin+" --> " +
                  str(mutado)+" = "+nuevoBin+"\n")
    return(mutado)


def crucess(individuos, generacion):
    hijos = []
    data = []
    max = []
    codificacion=[]
    numMax = 0
    generaciones = []
    cont = rango-1
    for i in range(1, generacion+1):  # obtine los i de los datos
        generaciones.append(i)

    for numGen in range(generacion):
        cont = rango-1
        nums = []
        data = []
        numMax=0
        if numGen==0:
            for x in range(len(individuos)):
                codificacion.append(individuos[x])
        for x in range(len(individuos)):
            if int(individuos[x]) >  int(numMax):
                numMax = individuos[x]
            data.append([individuos[x], codificacion[x]])
        max.append(numMax)
        codificacion = []
        for x in range(int(rango/2)):
            # print(x)
            hijo1,hijo2,mutado1,mutado2=generaHijo(individuos[x],individuos[cont])
            codificacion.append(hijo1)
            codificacion.append(hijo2)
            hijos.append(mutado1)
            hijos.append(mutado2)
            cont -= 1
        # print(' '.join(map(str, individuos)))
        # print(' '.join(map(str, hijos)))
        for i in range(1, len(individuos)+1):  # obtine los i de los datos
            nums.append(i)
        # agrega los datos de la tabla a data y saca el maximo
        # 
        #print(' '.join(map(str, nums)))
        # if individuos == hijos and numGen!=0:
        #     for i in range(2):
        #         rand = random.randint(0, len(hijos)-1)
        #         hijos[rand] = mutacion(hijos[rand])

        headers = ["Individuos", "Codificacion"]
        salidas.write("Generacion numero : "+str(numGen)+"\n")
        salidas.write(pandas.DataFrame(data, nums, headers).to_string())
        #elegirRandom(individuos) if generacion-1!= numGen else ""
        salidas.write("\n----------------------------------\n\n")

        individuos = hijos
        hijos = []
        

        if numGen == generacion-1:  # realiza la grafica
            datos = {'Generacion': generaciones, 'individuo': max}
            df = DataFrame(datos, columns=['Generacion', 'individuo'])
            df.plot(x='Generacion', y='individuo', kind='line')
            plt.show()

def generaHijo(padre,madre):
    binPadre = bin(padre)
    binMadre = bin(madre)
    #print(binPadre,binMadre,binPadre[0],binMadre[0])
    binPadre3, binPadre5, binMadre3, binMadre5 ="","","",""
    hijo1, hijo2 = "",""
    mutaPadre, mutaMadre, nuevoBin, mutado1,mutado2 = "", "","", 0,0
    #print(binPadre,binMadre)
    mutaPadre += "1" if binPadre[0] == "-" else "0"
    mutaMadre += "1" if binMadre[0] == "-" else "0"
    lonP =len(binPadre)-3 if binPadre[0] == "-" else len(binPadre)-2
    lonM =len(binMadre)-3 if binMadre[0] == "-" else len(binMadre)-2
    #print(lonP,lonM)
    for a in range(0, 9-lonP):
        mutaPadre += '0'
    for a in range(0, 9-lonM):
        mutaMadre += '0'
    
    signoP = 2 if mutaPadre[0] == "0" else 3
    signoM = 2 if mutaMadre[0] == "0" else 3

    for x in range(signoP, len(binPadre)):
        mutaPadre += binPadre[x]
    for x in range(signoM, len(binMadre)):
        mutaMadre += binMadre[x]
    
    
    #print(binPadre,binMadre,padre,madre)
    for i in range(1, len(mutaPadre)-1):
        if i >=1 and i <=3:
            binPadre3 += mutaPadre[i]
            binMadre3 += mutaMadre[i]
        else :
            binPadre5 += mutaPadre[i]
            binMadre5 += mutaMadre[i]
    hijo1=binPadre5+binMadre3
    hijo2=binMadre5+binPadre3
   # print(hijo1,hijo2)
    mutado1 = int(str(hijo1), 2)
    mutado2 = int(str(hijo2), 2)
    if binPadre[0] =="-":
        mutado1 =mutado1*(-1)
    if binMadre[0] =="-":
        mutado2 =mutado2*(-1) 
    #print(hijo1,hijo2,mutado1,mutado2)   
    return(hijo1,hijo2,mutado1,mutado2)

def crucecs(individuos, generacion):
    hijos = []
    data = []
    max = []
    codificacion=[]
    numMax = 0
    generaciones = []
    cont = rango-1
    for i in range(1, generacion+1):  # obtine los i de los datos
        generaciones.append(i)

    for numGen in range(generacion):
        cont = len(individuos)-1
        nums = []
        data = []
        numMax=0
        posX=0
        numMin=255
        if numGen==0:
            for x in range(len(individuos)):
                codificacion.append(individuos[x])
        for x in range(len(individuos)):
            if int(individuos[x]) >  int(numMax):
                numMax = individuos[x]
            data.append([individuos[x], codificacion[x]])
        max.append(numMax)
        codificacion = []
        for x in range(int(len(individuos)/2)):
            # print(x)
            hijo1,hijo2,mutado1,mutado2=generaHijo(individuos[x],individuos[cont])
            codificacion.append(hijo1)
            codificacion.append(hijo2)
            hijos.append(mutado1)
            hijos.append(mutado2)
            cont -= 1
        # print(' '.join(map(str, individuos)))
        # print(' '.join(map(str, hijos)))
        for i in range(1, len(individuos)+1):  # obtine los i de los datos
            nums.append(i)
        # agrega los datos de la tabla a data y saca el maximo
        # 
        #print(' '.join(map(str, nums)))
        # if individuos == hijos and numGen!=0:
        #     for i in range(2):
        #         rand = random.randint(0, len(hijos)-1)
        #         hijos[rand] = mutacion(hijos[rand])
        for i in range(2):
            for x in range(len(hijos)):
                if int(hijos[x]) <  int(numMin):
                    numMin = hijos[x]
                    posX=x
            hijos.pop(posX)
        headers = ["Individuos", "Codificacion"]
        salidas.write("Generacion numero : "+str(numGen)+"\n")
        salidas.write(pandas.DataFrame(data, nums, headers).to_string())
        #elegirRandom(individuos) if generacion-1!= numGen else ""
        salidas.write("\n----------------------------------\n\n")

        individuos = hijos
        hijos = []
        

        if numGen == generacion-1:  # realiza la grafica
            datos = {'Generacion': generaciones, 'individuo': max}
            df = DataFrame(datos, columns=['Generacion', 'individuo'])
            df.plot(x='Generacion', y='individuo', kind='line')
            plt.show()


rango, generacion, metodo = leer()
individuos = crear(rango)
ruleta(individuos, generacion, rango) if metodo == 0 else torneo(individuos, generacion,
                                                                 rango) if metodo == 1 else crucess(individuos, generacion) if metodo == 2 else crucecs(individuos, generacion)
