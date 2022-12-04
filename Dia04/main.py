fichero = open('datos.txt')
lista = []
for linea in fichero:
    lista.append(linea.rstrip())
finalizado = False
linea = 0
puntos = 0
items_1 = []
items_2 = []
condicion = False
while not finalizado:
    try:
        line = lista[linea].split(",")
        line_1 = line[0].split("-")
        line_2 = line[1].split("-")
        for i in line_1:
            items_1.append(int(i))
        for j in line_2:
            items_2.append(int(j))
        if items_1[-2] >= items_2[-2] and items_1[-1] <= items_2[-1]:
            puntos += 1
        elif items_2[-2] >= items_1[-2] and items_2[-1] <= items_1[-1]:

            puntos += 1

        linea += 1
        condicion = False
        items_1 = []
        items_2 = []
    except:
        finalizado = True


print(puntos)



finalizado = False
linea = 0
puntos = 0
items_1 = []
items_2 = []
condicion = False
while not finalizado:
    try:
        puntos+=1
        line = lista[linea].split(",")
        line_1 = line[0].split("-")
        line_2 = line[1].split("-")
        for i in line_1:
            items_1.append(int(i))
        for j in line_2:
            items_2.append(int(j))
        if items_1[-2] <  items_2[-2] and items_1[-1] < items_2[-2]:
            puntos -= 1
        elif items_2[-2] < items_1[-2] and items_2[-1] < items_1[-2]:
            puntos -= 1
        elif items_1[-2] > items_2[-1] and items_1[-1] >  items_2[-1]:
            puntos -= 1
        elif items_2[-2] > items_1[-1] and items_2[-1] >  items_1[-1]:
            puntos -= 1

        linea += 1
        condicion = False
        items_1 = []
        items_2 = []
    except:
        finalizado = True

print(puntos-1)