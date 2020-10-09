posX=[[0 for x in range(50)] for y in range(50)]
posY=[[0 for x in range(50)] for y in range(50)]
estado=[[0 for x in range(50)] for y in range(50)]
estadoAux=[[0 for x in range(50)] for y in range(50)]
ancho=15
x2=0
for x in range(50):
    y2=0
    for y in range(50):
        posY[x][y]=y2
        posX[x][y]=x2
        estado[x][y]=0
        y2=y2+ancho
    x2=x2+ancho
def paso():
    global posY, posX, estado,ancho,estadoAux
    vecinos=0
    for y in range(50):
        for x in range(50):
            estadoAux=[[0 for x in range(50)] for y in range(50)]
            checaVecinos(x,y)
            
    estado=estadoAux
    

def checaVecinos(x,y):
    global estado
    aux1,aux2,aux3,aux4= checar(x+49),checar(x+51),checar(y+49),checar(y+51)
    
    suma=estado[aux1][y] +estado[aux2][y] +estado[x][aux3] +estado[x][aux4] +estado[aux1][aux3] +estado[aux2][aux3] +estado[aux1][aux4] +estado[aux1][aux4] 
    print(x,aux1,aux2,aux3,aux4, suma)
    if (suma ==2 or suma ==3) and estado[x][y]==1 :
        estadoAux[x][y]=1
    elif suma ==3 and estado[x][y]==0:
        estadoAux[x][y]=1
    else:
        estadoAux[x][y]=0
def checar(num):   
    if num>49:
        while(num>49):
            num=num-50
        return num
    else:
        return num  
paso()

    print(y,x,aux1,aux2,aux3,aux4, suma)