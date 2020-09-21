# Created by María Fernanda Lua Morales and Brian Daniel Frausto Cortés on 09/11/2020
# Este programa está diseñado para solucionar oraciones complejas de lógica proposicional.  

variables = []
sentencias = []
verdad = []
sentcomp = ["NO", "Y", "ENTONCES", "O", "SI", "IGUAL A", "ES"]
sc = ["~", "^", "->", "v", "?", "=", "?"]
#################################################################################################
# Método para leer entradas del archivo txt

def leer():
    archivo = open("entradas.txt", "r")
    entrada = archivo.readlines()
    r = 0
    for renglon in entrada:
        cont = 0
        r += 1
        for ver in renglon.split(","):
            ver = ver.rstrip()
            if cont == 0:
                variables.append(ver)
            if cont == 1:
                sentencias.append(ver),
            if cont == 2:
                verdad.append(ver)
            cont += 1
            if cont == 3:
                cont = 0
    return r

#################################################################################################
# Método para reemplazar oración compleja en variables, convertir variables a valores de verdad

def mostrar(cadena, rango):
    cadena = cadena.upper()
    for a in range(rango):
        sentenci = sentencias[a]                ##Se cambian las oraciones complejas por variables 
        cadena = cadena.replace(sentenci.upper(), variables[a])
    for a in range(7):                          ##Se cambian las sentencias complejas por simbolos
        cadena = cadena.replace(sentcomp[a], sc[a])
    cadena = quitarespacio(cadena)
    print(cadena)
    for a in range(rango):                      ##Se cambian las variables por valores de verdad
        cadena = cadena.replace(variables[a], verdad[a])
    print(cadena)
    evalua(cadena)

#################################################################################################
#Método para quitar espacios en donde aparece el caracter ?

def quitarespacio(cadena):
    subcadena = ""
    for caracter in cadena.split(" "):
        if caracter != "?":
            subcadena += caracter+" "
    return subcadena

#################################################################################################
##Método para evaluar la sentensian compleja

def evalua(cadena):
    cadena = evaluanegacion(cadena)     ##evalua la negacion y elimina el simbolo ~
    print(cadena)
    by = False
    bo = False
    ben = False
    big = False
    var1 = ""
    var2 = ""
    contvar = 0
    cadena2 = cadena
    for caracter in cadena.split(" "):
        if caracter == "F" or caracter == "V":
            contvar += 1
            if contvar == 1:
                var1 = caracter
            else:
                var2 = caracter
                contvar = 0
                if by:
                    caracter, cadena2 = evaluay(cadena2, var1, var2)     ##evalua la conjunción y elimina el simbolo ^
                    print(cadena2)
                    var1 = caracter
                    contvar += 1
                    by = False
                elif bo:
                    caracter, cadena2 = evaluao(cadena2, var1, var2)     ##evalua la disyunción y elimina el simbolo v
                    print(cadena2)
                    var1 = caracter
                    contvar += 1
                    bo = False
                elif ben:
                    caracter, cadena2 = evaluaen(cadena2, var1, var2)    ##evalua la condicion-material(entonces) y elimina el simbolo ->
                    print(cadena2)
                    var1 = caracter
                    contvar += 1
                    ben = False
                elif big:
                    caracter, cadena2 = evaluabig(cadena2, var1, var2)   ##evalua la igual y elimina el simbolo =
                    print(cadena2)
                    var1 = caracter
                    contvar += 1
                    big = False
        elif caracter == "^":
            by = True
        elif caracter == "v":
            bo = True
        elif caracter == "->":
            ben = True
        elif caracter == "=":
            big = True
    print(caracter)

#################################################################################################
##Método que evalua la negacion y elimina el simbolo ~

def evaluanegacion(cadena):
    subcadena = ""
    bno = False
    for caracter in cadena.split(" "):
        if caracter == "~":
            bno = True
        elif caracter == "F":
            if bno:
                subcadena += "V "
                bno = False
            else:
                subcadena += caracter+" "
        elif caracter == "V":
            if bno:
                subcadena += "F "
                bno = False
            else:
                subcadena += caracter+" "
        else:
            subcadena += caracter+" "
    return subcadena

#################################################################################################
##Método que evalua la conjunción y elimina el simbolo ^

def evaluay(cadena, var1, var2):
    subcadena = ""
    caracter = ""
    quitar = var1+" ^ "+var2
    if var1 == "V" and var2 == "V":
        caracter = "V"
        subcadena = cadena.replace(quitar, caracter)
    elif var1 == "V" and var2 == "F":
        caracter = "F"
        subcadena = cadena.replace(quitar, caracter)
    elif var1 == "F" and var2 == "V":
        caracter = "F"
        subcadena = cadena.replace(quitar, caracter)
    else:
        caracter = "F"
        subcadena = cadena.replace(quitar, caracter)
    return caracter, subcadena

#################################################################################################
##evalua la disyunción y elimina el simbolo v

def evaluao(cadena, var1, var2):
    subcadena = ""
    caracter = ""
    quitar = var1+" v "+var2
    if var1 == "V" and var2 == "V":
        caracter = "V"
        subcadena = cadena.replace(quitar, caracter)
    elif var1 == "V" and var2 == "F":
        caracter = "V"
        subcadena = cadena.replace(quitar, caracter)
    elif var1 == "F" and var2 == "V":
        caracter = "V"
        subcadena = cadena.replace(quitar, caracter)
    else:
        caracter = "F"
        subcadena = cadena.replace(quitar, caracter)
    return caracter, subcadena

#################################################################################################
##Método que evalua la condicion-material(entonces) y elimina el simbolo ->

def evaluaen(cadena, var1, var2):
    subcadena = ""
    caracter = ""
    quitar = var1+" -> "+var2
    if var1 == "V" and var2 == "V":
        caracter = "V"
        subcadena = cadena.replace(quitar, caracter)
    elif var1 == "V" and var2 == "F":
        caracter = "F"
        subcadena = cadena.replace(quitar, caracter)
    elif var1 == "F" and var2 == "V":
        caracter = "V"
        subcadena = cadena.replace(quitar, caracter)
    else:
        caracter = "V"
        subcadena = cadena.replace(quitar, caracter)
    return caracter, subcadena

#################################################################################################
##Método que evalua la igual y elimina el simbolo =

def evaluabig(cadena, var1, var2):
    subcadena = ""
    caracter = ""
    quitar = var1+" = "+var2
    if var1 == "V" and var2 == "V":
        caracter = "V"
        subcadena = cadena.replace(quitar, caracter)
    elif var1 == "V" and var2 == "F":
        caracter = "F"
        subcadena = cadena.replace(quitar, caracter)
    elif var1 == "F" and var2 == "V":
        caracter = "F"
        subcadena = cadena.replace(quitar, caracter)
    else:
        caracter = "V"
        subcadena = cadena.replace(quitar, caracter)
    return caracter, subcadena

#################################################################################################
# Clase Main

rango = leer()
if 2 <= rango <= 4:
    cadena = input("Ingrese una sentencia compleja\n")
    mostrar(cadena, rango)
else:
    print("Recuerde ingresar el número de sentencias permitidas (min 2, max 4)")
