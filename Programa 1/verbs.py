def regular(verbo,conjj,conjugado):
    conjugado.append(conj+"o")
    conjugado.append(conjj+"s")
    conjugado.append(conjj)
    conjugado.append(conjj+"mos")
    conjugado.append(conjj+"n")
    for arr in conjugado:    
        reg.write(arr+",")
    reg.write("\n")
##############################################
def irregular(conjugado):
    conjugado.append(input("Yo: "))
    conjugado.append(input("Tú: "))
    conjugado.append(input("Él: "))
    conjugado.append(input("Nosotros: "))
    conjugado.append(input("Ustedes: "))
    for arr in conjugado:    
        irreg.write(arr+",")
    irreg.write("\n")
##############################################
def conjugar(verbo,conj,conjj):
    conjugado=[]
    print("Yo ",conj+"o")
    print("Tú ",conjj+"s")
    print("Él ",conjj)
    print("Nosotros ",conjj+"mos")
    print("Ellos",conjj+"n")
    conjugado.append(verbo)
    a=input("¿Es correcto? (Y-y/N-n): ")
    if a=="Y" or a=="y":
        regular(verbo,conjj,conjugado)
    else:
        irregular(conjugado)
##############################################        
def verificar(verbo):
    data=reg.readlines()
    dato=irreg.readlines()
    for renglon in data:
        cont=0
        band=False
        for ver in renglon.split(","):
            if verbo==ver:
                band=True
            if cont==1:
                print("Yo ",ver)
            if cont==2:
                print("Tú ",ver)
            if cont==3:
                print("Él ",ver)
            if cont==4:
                print("Nosotros ",ver)
            if cont==5:
                print("Ellos",ver)
                return False
            if band:
                cont+=1             
    for renglon in dato:
        cont=0
        band=False
        for ver in renglon.split(","):
            if verbo==ver:
                band=True
            if cont==1:
                print("Yo ",ver)
            if cont==2:
                print("Tú ",ver)
            if cont==3:
                print("Él ",ver)
            if cont==4:
                print("Nosotros ",ver)
            if cont==5:
                print("Ellos",ver)
                return False
            if band:
                cont+=1  
    return True     
###########################################
reg=open('/mnt/SSD/Users/briar/Documents/6TO_SEMESTRE/Prog_Lógica_y_Func/Python/Regular.txt','r+')
irreg=open('/mnt/SSD/Users/briar/Documents/6TO_SEMESTRE/Prog_Lógica_y_Func/Python/Irregular.txt','r+')
print("Ingresa el verbo")
verbo=input()
if verificar(verbo):
    conj=""
    conjj=""
    cont=0
    for letra in verbo:
        cont+=1
        if cont < len(verbo)-1:
            conj+=letra
        if cont < len(verbo):
            conjj+=letra
    conjugar(verbo,conj,conjj)