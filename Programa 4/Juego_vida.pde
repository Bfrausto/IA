posX=[[0 for x in range(50)] for y in range(50)]
posY=[[0 for x in range(50)] for y in range(50)]
estado=[[0 for x in range(50)] for y in range(50)]
estadoAux=[[0 for x in range(50)] for y in range(50)]
ancho=15
def setup():
    size(1000,750)
    background(51, 51, 153)
    image(loadImage("button_paso-a-paso.png"), 800, 20,147,44)
    image(loadImage("button_evolucion.png"), 800, 84,147,44)
    image(loadImage("button_random.png"), 800, 148,147,44)
    image(loadImage("button_pausa.png"), 800, 212,147,44)
    image(loadImage("button_limpiar.png"), 800, 650,147,44)

x2=0    
for x in range(50):
    y2=0
    for y in range(50):
        posY[x][y]=y2
        posX[x][y]=x2
        estado[x][y]=0
        y2=y2+ancho
    x2=x2+ancho

def draw():
    if mouseX < 750:
        cursor(CROSS)
    elif mouseX>=800 and mouseX<=947 and mouseY>=20 and mouseY<=64:
        cursor(HAND)
    global posY, posX, estado,ancho
    for x in range(50):
        for y in range(50):
            if estado[x][y]==0: 
                fill(255);
            else :
                fill(0)
            rect(posX[x][y],posY[x][y],ancho,ancho)

def mouseClicked(): 
    global posY, posX, estado,ancho
    for x in range(50):
        for y in range(50):
            if mouseX>=posX[x][y] and mouseX<posX[x][y]+ancho and mouseY>=posY[x][y] and mouseY<posY[x][y]+ancho:
                colorear(x,y)
                break
    if mouseX>=800 and mouseX<=947 and mouseY>=20 and mouseY<=64:
        paso()

def paso():
    global posY, posX, estado,ancho,estadoAux
    vecinos=0
    for y in range(50):
        for x in range(50):
            checaVecinos(x,y)
    estado=estadoAux
    estadoAux=[[0 for x in range(50)] for y in range(50)]
    

def checaVecinos(x,y):
    global estado,estadoAux
    aux1,aux2,aux3,aux4= checar(x+49),checar(x+51),checar(y+49),checar(y+51)
    suma=estado[aux1][y] +estado[aux2][y] +estado[x][aux3] +estado[x][aux4] +estado[aux1][aux3] +estado[aux2][aux3] +estado[aux1][aux4] +estado[aux2][aux4] 
    
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

def colorear(x,y):  
    global estado
    if estado[x][y] ==0:
        estado[x][y] =1
    else:
        estado[x][y] =0