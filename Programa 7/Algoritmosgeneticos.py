poblacion=
def leer():
    archivo = open("entrada.txt", "r")
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
    return r
rango = leer()
# from pandas import DataFrame
# import matplotlib.pyplot as plt
   
# Data = {'Year': [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010],
#         'Unemployment_Rate': [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
#        }
  
# df = DataFrame(Data,columns=['Year','Unemployment_Rate'])
# df.plot(x ='Year', y='Unemployment_Rate', kind = 'line')
# plt.show()