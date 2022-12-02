fichero = open('datos.txt')
lista = []
for linea in fichero:
    
    lista.append(linea.split())
finalizado = False
i = 1
linea = 0

while not finalizado:
    try:
        locals()["duende"+str(i)] = 0
        while lista[linea] != []:
            
            locals()["duende"+str(i)] += int(lista[linea][0])
            linea += 1

        linea += 1
        i += 1
    except:
        finalizado = True

duende_1 = 0
duende_2 = 0
duende_3 = 0

for k in range(1, i + 1):
    if locals()["duende"+str(k)] > duende_1:
        duende_1 = locals()["duende"+str(k)]

lista_max = []
for k in range(1, i + 1):
    lista_max.append(locals()["duende"+str(k)])

lista_max.sort(reverse = True)
print(lista_max[0])
print(lista_max[1])
print(lista_max[2])


print(lista_max[0]+lista_max[1]+lista_max[2])
