archivo = open("entradas.txt", "r")
entrada=archivo.readlines()
    for renglon in entrada:
        cont=0
        band=False
        for ver in renglon.split(","):
             print(ver)          
    