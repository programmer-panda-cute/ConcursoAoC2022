fichero = open('datos.txt')
lista = []
for linea in fichero:
    lista.append(linea.rstrip())
finalizado = False
linea = 0
puntos = 0
items_repetidos = []
condicion = False
while not finalizado:
    try:

        items_por_compartimento = int(len(lista[linea]) / 2)
        print(lista[linea])
        lista[linea] = lista[linea][:items_por_compartimento] + ":" + lista[linea][items_por_compartimento:]
        print(lista[linea])
        line = lista[linea].split(":")
        for item in line[0]:
            if item in line[1] and condicion == False:
                print(item)
                items_repetidos.append(item)
                condicion = True

        linea += 1
        condicion = False
    except:
        finalizado = True

for item in items_repetidos:
    if item == item.lower():
        puntos += ord(item) - ord('a') + 1
    else:
        puntos += ord(item) - ord('A') + 27
print(puntos)



fichero = open('datos.txt')
lista = []
for linea in fichero:
    lista.append(linea.rstrip())
finalizado = False
linea = 0

puntos = 0
items_repetidos = []

condicion = False
while not finalizado:
    try:

        for item in lista[linea]:
            if item in lista[linea+1] and condicion == False and item in lista[linea+2]:
                print(item)
                items_repetidos.append(item)
                condicion = True

        linea += 3
        condicion = False
    except:
        finalizado = True

for item in items_repetidos:
    if item == item.lower():
        puntos += ord(item) - ord('a') + 1
    else:
        puntos += ord(item) - ord('A') + 27
print(puntos)