posX=[]
posY=[]
estado=[]
ancho=15
def setup():
    size(1000,750)
    background(51, 51, 153)
    image(loadImage("button_paso-a-paso.png"), 800, 20,147,44)
    image(loadImage("button_evolucion.png"), 800, 84,147,44)
    image(loadImage("button_random.png"), 800, 148,147,44)
    image(loadImage("button_limpiar.png"), 800, 650,147,44)

y2=0    
for y in range(50):
    x2=0
    for x in range(50):
        posY.append(y2)
        posX.append(x2)
        estado.append(255)
        x2=x2+ancho
    y2=y2+ancho

def draw():
    if mouseX < 750:
        cursor(CROSS)
    else:
        cursor(HAND)
    global posY, posX, estado,ancho
    for i in range(len(estado)):
        fill(estado[i]);
        rect(posX[i],posY[i],ancho,ancho)

def mouseClicked(): 
    global posY, posX, estado,ancho
    for i in range(len(estado)):
        if mouseX>=posX[i] and mouseX<posX[i]+ancho and mouseY>=posY[i] and mouseY<posY[i]+ancho:
            if estado[i] ==255:
                estado[i] =0
            else:
                estado[i] =255
    

