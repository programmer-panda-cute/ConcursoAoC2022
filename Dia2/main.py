fichero = open('datos.txt')
lista = []
for linea in fichero:
    
    lista.append(linea.split())
finalizado = False
linea = 0
puntos = 0

#primero mi oponente y luego yo
while not finalizado:
    try:
        if lista[linea][0] == "A" : #Roca
            if lista[linea][1] == "X":#Roca:
                puntos += 1
                puntos += 3
            elif lista[linea][1] == "Y":#Papel:
                puntos += 2
                puntos  += 6
            elif lista[linea][1] == "Z":#Tijeras:
                puntos += 3

        elif lista[linea][0] == "B":#Papel
            if lista[linea][1] == "X":#Roca:
                puntos += 1
            elif lista[linea][1] == "Y":#Papel:
                puntos += 2
                puntos += 3
            elif lista[linea][1] == "Z":#Tijeras:
                puntos += 3
                puntos += 6
        
        else:#Tijeras
            if lista[linea][1] == "X":#Roca:
                puntos += 1
                puntos += 6
            elif lista[linea][1] == "Y":#Papel:
                puntos += 2
            elif lista[linea][1] == "Z":#Tijeras:
                puntos += 3
                puntos += 3
        linea += 1
    except:
        finalizado = True

print("puntos totales: ", puntos)

# X necesito perder
# Y necesito empatar
# Z necesito ganar

linea = 0
puntos = 0
finalizado = False
while not finalizado:
    try:
        if lista[linea][0] == "A" : #Roca
            if lista[linea][1] == "X":#Debo perder:
                puntos += 3
            elif lista[linea][1] == "Y":#Debo empatar:
                puntos += 1
                puntos  += 3
            elif lista[linea][1] == "Z":#Debo ganar:
                puntos += 2
                puntos += 6

        elif lista[linea][0] == "B":#Papel
            if lista[linea][1] == "X":#Debo perder:
                puntos += 1
            elif lista[linea][1] == "Y":#Debo empatar:
                puntos += 2
                puntos += 3
            elif lista[linea][1] == "Z":#Debo ganar:
                puntos += 3
                puntos += 6
        
        else:#Tijeras
            if lista[linea][1] == "X":#Debo perder:
                puntos += 2
            elif lista[linea][1] == "Y":#Debo empatar:
                puntos += 3
                puntos += 3
            elif lista[linea][1] == "Z":#Debo ganar:
                puntos += 1
                puntos += 6
        linea += 1
    except:
        finalizado = True

print("puntos totales: ", puntos)
