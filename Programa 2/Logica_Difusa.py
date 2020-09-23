variable = []
rangoinf = []
rangosup = []
valores = []
medias = []
#################################################################################################
# Método para leer entradas del archivo txt


def leer():
    archivo = open("entradas.txt", "r")
    entrada = archivo.readlines()
    archivo2 = open("valores.txt", "r")
    entrada2 = archivo2.read()
    r = 0
    for renglon in entrada:
        cont = 0
        r += 1
        for ver in renglon.split(","):
            ver = ver.rstrip()
            if cont == 0:
                variable.append(ver)
            if cont == 1:
                rangoinf.append(int(ver)),
            if cont == 2:
                rangosup.append(int(ver))
            cont += 1
            if cont == 3:
                cont = 0

    for ver2 in entrada2.split(","):
        ver2 = ver2.rstrip()
        valores.append(float(ver2))

    # for a,b,c in zip(variable,rangoinf,rangosup):
    #     print(a,b,c)
    return r

#################################################################################################
# Se verifica el traslape


def verTraslape():
    auxInfAct = 0
    auxSupant = 0
    band = False
    for a, b in zip(rangoinf, rangosup):
        if band:
            auxInfAct = a
            band = False
        if auxInfAct > auxSupant:
            print("No existe Traslape entre los rangos")
            break
        if not band:
            auxSupant = b
            band = True

#################################################################################################
# se obtienen las medias de los rangos


def obtenerMedia():
    for a, b in zip(rangoinf, rangosup):
        medias.append((a+b)/2)
   # for a in medias:
   #    print (a)

#################################################################################################
# se crea el archivo de salidas y se definen los valores de variables


def funcionMembresia(rango):
    salidas = open("salida.txt", "w")
    salidas.write('Valor\tGrado\tRango\tDescripcion\n')
    for x in valores:
        cont = 0
        c = 0
        auxValorVerdad = 0
        auxRangoInf = 0
        auxRangoSup = 0
        auxVariable = " "
        for a, d, b, var in zip(rangoinf, rangosup, medias, variable):
            if cont == 0:
                c = b
                b = a
                if x < a:
                    auxRangoInf = a  # valores menores al rango menor
                    auxRangoSup = d
                    auxVariable = var

            elif cont == rango-1:
                c = d
                if x > d:
                    auxRangoInf = a  # valores mayores al rango mayor
                    auxRangoSup = d
                    auxVariable = var
            else:
                c = b
            cont += 1
            valorVerdad = float(evaluaX(a, b, c, d, x))
            if valorVerdad > auxValorVerdad:
                auxValorVerdad = valorVerdad  # guarda los valores que se mostraran el el txt
                auxRangoInf = a
                auxRangoSup = d
                auxVariable = var
        salidas.write(str(x)+'  \t'+str(round(auxValorVerdad, 3))+'  \t' +
                      str(auxRangoInf)+'-'+str(auxRangoSup)+' \t'+auxVariable+'\n')
    salidas.close()


#################################################################################################
# evaluar el valor en la funcion de membresia

def evaluaX(a, b, c, d, x):
    if x <= a:
        return 0
    elif a <= x and x <= b:
        return ((x-a)/(b-a))
    elif b <= x and x <= c:
        return 1
    elif c <= x and x <= d:
        return ((d-x)/(d-c))
    else:
        return 0

#################################################################################################
# Clase Main


rango = leer()
cadena = 0
if 2 <= rango <= 4:
    verTraslape()
    obtenerMedia()
    funcionMembresia(rango)
else:
    print("Recuerde ingresar el número de rangos permitidos (min 2, max 4)")
