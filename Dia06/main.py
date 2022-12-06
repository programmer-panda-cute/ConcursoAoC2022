fichero = open('datos.txt')
lista = []
for linea in fichero:
    lista.append(linea)
finalizado = False
linea = 0

condicion = False


lista = list(lista[linea].split()[0])
while not finalizado:
    try:
        pos = 0
        for i in range(0, len(lista)):

            if lista[i] != lista[i+1] and lista[i] != lista[i+2] and lista[i] != lista[i+3] and lista[i+1] != lista[i+2] and lista[i+1] != lista[i+3] and lista[i+2] != lista[i+3]:
                print(i+4)
                finalizado = True
                break

               

        i+=1
    except:
        finalizado = True





fichero = open('datos.txt')
lista = []
for linea in fichero:
    lista.append(linea)
# print(lista)
finalizado = False

condicion = False
linea = 0

lista = list(lista[linea].split()[0])
def lastindexof (lista, elemento):
    for i in range(len(lista)-1, -1, -1):
        if lista[i] == elemento:
            return i
    return -1
while not finalizado:

    for i in range(0, len(lista)):

        sublista = lista[i:i + 14]
        u = lista[i]
        sublista.pop(0)
        h = 0
        while (len(sublista) > 0 and not condicion): 
            h+=1
            if not condicion:
                for j in sublista:
                    if j == u:
                        condicion = True
                        break
                u = sublista[0]
                sublista.pop(0)        
        if not condicion:
            finalizado = True
            print(i+14)
            break
        condicion = False
            

