posx=[]
posy=[]
colores=[]
ancho=20
y2=0    
for y in range(50):
    x2=0
    for x in range(50):
        posy.append(y2)
        posx.append(x2)
        colores.append(255)
        x2=x2+ancho
    y2=y2+ancho

for i in range(len(colores)):
        print(posx[i],posy[i],colores[i])
        