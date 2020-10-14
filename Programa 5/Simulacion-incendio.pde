#Created by María Fernanda Lua Morales and Brian Daniel Frausto Cortés on 10/05/2020
#Este programa simula el comportamiento de Autómatas Celulares de Dimensión 1 
import random
posX=[[0 for x in range(50)] for y in range(50)]
posY=[[0 for x in range(50)] for y in range(50)]
estado=[[0 for x in range(50)] for y in range(50)]
estadoAux=[[0 for x in range(50)] for y in range(50)]
ancho=15
gen=0
ejecutar=False
time=0
def setup():
    size(1000,750)
    background(51, 51, 153)
    textSize(15)
    text("Generacion no: ",800,300)
    gene()
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
        estado[x][y]=3
        y2=y2+ancho
    x2=x2+ancho

def draw():
    global time,posY, posX, estado,ancho
    if mouseX>=800 and mouseX<=947 and mouseY>=20 and mouseY<=64:
        cursor(HAND)
    elif mouseX>=800 and mouseX<=947 and mouseY>=84 and mouseY<=128:
        cursor(HAND)
    elif mouseX>=800 and mouseX<=947 and mouseY>=148 and mouseY<=192:
        cursor(HAND)
    elif mouseX>=800 and mouseX<=947 and mouseY>212 and mouseY<=256:
        cursor(HAND)
    elif mouseX>=800 and mouseX<=947 and mouseY>=650 and mouseY<=694:
        cursor(HAND)
    elif mouseX<750:
        cursor(CROSS)
    else:
        cursor(ARROW)
    
    for x in range(50):
        for y in range(50):
            if estado[x][y]==0: 
                fill(153, 153, 153)
            elif estado[x][y]==1: 
                fill(255, 58, 22)
            elif estado[x][y]==2:
                fill(26, 199, 37)
            else:
                fill(255)
            rect(posX[x][y],posY[x][y],ancho,ancho)
    if ejecutar:
        paso()
        delay(time)    

def mousePressed(): 
    global posY, posX, estado,ancho
    if mouseButton == LEFT:
        for x in range(50):
            for y in range(50):
                if mouseX>=posX[x][y] and mouseX<posX[x][y]+ancho and mouseY>=posY[x][y] and mouseY<posY[x][y]+ancho:
                    colorear(x,y)
                    break
        if mouseX>=800 and mouseX<=947 and mouseY>=20 and mouseY<=64:
            paso()
        if mouseX>=800 and mouseX<=947 and mouseY>=84 and mouseY<=128:
            evolucion()
        if mouseX>=800 and mouseX<=947 and mouseY>=148 and mouseY<=192:
            aleatorio()
        if mouseX>=800 and mouseX<=947 and mouseY>212 and mouseY<=256:
            pausa()
        if mouseX>=800 and mouseX<=947 and mouseY>=650 and mouseY<=694:
            limpiar()
    if mouseButton == RIGHT:
        for x in range(50):
            for y in range(50):
                if mouseX>=posX[x][y] and mouseX<posX[x][y]+ancho and mouseY>=posY[x][y] and mouseY<posY[x][y]+ancho:
                    colorearB(x,y)
                    break


def paso():
    global posY, posX, estado,ancho,estadoAux,gen
    gen=gen+1
    gene()
    for y in range(50):
        for x in range(50):
            checaVecinos(x,y)
    estado=estadoAux
    estadoAux=[[2 for x in range(50)] for y in range(50)]   

def checaVecinos(x,y):
    global estado,estadoAux
    aux1,aux2,aux3,aux4= checar(x+49),checar(x+51),checar(y+49),checar(y+51)
    sumaC,sumaA,sumaF,sumaM=0,0,0,0
    auxsuma=[estado[aux1][y],estado[aux2][y] ,estado[x][aux3] ,estado[x][aux4] ,estado[aux1][aux3] ,estado[aux2][aux3] ,estado[aux1][aux4] ,estado[aux2][aux4] ]
    for a in auxsuma:
        if a==0:
            sumaC=sumaC+1
        elif a==1:
            sumaF=sumaF+1
        elif a==2:
            sumaA=sumaA+1
        elif a==3:  
            sumaM=sumaM+1
   # print(sumaC,sumaF,sumaA)
   # print(x,y,estado[x][y])
    suma=estado[aux1][y] +estado[aux2][y] +estado[x][aux3] +estado[x][aux4] +estado[aux1][aux3] +estado[aux2][aux3] +estado[aux1][aux4] +estado[aux2][aux4] 
    if estado[x][y]==3:
        estadoAux[x][y]=3
    elif estado[x][y]==0:
        if sumaC>=4 and sumaC<=8:
            estadoAux[x][y]=0
        elif sumaC>=1 and sumaC<=3:
            estadoAux[x][y]=0
        elif sumaM ==8:
            estadoAux[x][y]=3
        elif sumaF>=1 and sumaF<=8:
            estadoAux[x][y]=0
        elif sumaA>=4 and sumaA<=8:
            estadoAux[x][y]=0
        elif sumaA>=1 and sumaA<=3:
            estadoAux[x][y]=0
    elif estado[x][y]==1:
        if sumaC>=2 and sumaC<=8:
            estadoAux[x][y]=0
        elif sumaC>0 and sumaC<=1:
            estadoAux[x][y]=1
        elif sumaM ==8:
            estadoAux[x][y]=1
        elif sumaF>=4 and sumaF<=8:
            estadoAux[x][y]=0
        elif sumaF>=1 and sumaF<=3:
            estadoAux[x][y]=1
        elif sumaA>=1 and sumaA<=8:
            estadoAux[x][y]=1
    elif estado[x][y]==2:
        if (sumaF>=1 and sumaF<=8) :
            estadoAux[x][y]=1
        elif (sumaC>=0 and sumaC<=8) or (sumaA>=1 and sumaA<=8):
            estadoAux[x][y]=2
   # print(x,y,estadoAux[x][y])
    #print("  ")
def checar(num):   
    if num>49:
        while(num>49):
            num=num-50
    return num 

def limpiar():
    global gen
    for x in range(50):
        for y in range(50):
            estado[x][y]=3
    gen=0
    gene()
    pausa()

def aleatorio():
    for x in range(50):
        for y in range(50):
            estado[x][y]=random.randint(2, 3)

def evolucion():
    global ejecutar
    ejecutar=True
   
def pausa():
    global ejecutar
    ejecutar=False

def gene():
    global gen
    fill(51, 51, 153)
    noStroke()
    rect(920, 280, 100, 32)
    fill(255)
    textSize(15)
    text(gen,920,300)
    stroke(0)

def colorear(x,y):  
    global estado
    if estado[x][y] ==2:
        estado[x][y] =1
    else:
        estado[x][y] =2

def colorearB(x,y):  
    global estado
    if estado[x][y] ==3:
        estado[x][y] =2
    else:
        estado[x][y] =3