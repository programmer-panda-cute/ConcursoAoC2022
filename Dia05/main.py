fichero = open('datos.txt')
lista = []
for linea in fichero:
    lista.append(linea)
# print(lista)
finalizado = False
linea = 0
puntos = 0
items_1 = []
items_2 = []
condicion = False
movimientos = []


#     [V] [G]             [H]        
# [Z] [H] [Z]         [T] [S]        
# [P] [D] [F]         [B] [V] [Q]    
# [B] [M] [V] [N]     [F] [D] [N]    
# [Q] [Q] [D] [F]     [Z] [Z] [P] [M]
# [M] [Z] [R] [D] [Q] [V] [T] [F] [R]
# [D] [L] [H] [G] [F] [Q] [M] [G] [W]
# [N] [C] [Q] [H] [N] [D] [Q] [M] [B]
#  1   2   3   4   5   6   7   8   9 

#move 3 from 2 to 5
#mover 3 cajas de la pila 2 a la pila 5
#se muebve lo que está arriba del todo es decir primer elemento de la pila
for i in range (1, 10):
    locals()["pila"+str(i)] = []

while not finalizado:
    try:
        
    #lista[linea] = lista[linea].split() 
        pos = 0
        if lista[linea].split() != []:
            print(lista[linea])
            print(len(lista[linea]))
            print(lista[linea].split())

            if (lista[linea].split()[0] != 'move' and lista[linea].split()[0] != '1'):
                for char in lista[linea]:
                    if str(char) != ' ':
                        if pos%2 != 0:
                            print(char)
                            if pos == 1:
                                pila1.append(char)
                            elif pos == 5:
                                pila2.append(char)
                            elif pos == 9:
                                pila3.append(char)
                            elif pos == 13:
                                pila4.append(char)
                            elif pos == 17:
                                pila5.append(char)
                            elif pos == 21:
                                pila6.append(char)
                            elif pos == 25:
                                pila7.append(char)
                            elif pos == 29:
                                pila8.append(char)
                            elif pos == 33:
                                pila9.append(char)
                    pos+=1
            else:
                if lista[linea].split()[0] == 'move':
                    for i in range(1, int(lista[linea].split()[1]) + 1):
                        x = lista[linea].split()[3]
                        y = lista[linea].split()[5]
                        print(x)
                        print(y)
                        print(lista[linea])
                        print(locals()["pila" + str(y)] )
                        print(locals()["pila" + str(x)] )
                        locals()["pila"+str(y)].insert(0, locals()["pila"+str(x)][0])
                        locals()["pila"+str(x)].pop(0)
                        print(locals()["pila" + str(y)] )
                        print(locals()["pila" + str(x)] )                        

        linea+=1
    except:
        finalizado = True


print(movimientos)
print(pila1[0] + pila2[0] + pila3[0] + pila4[0] + pila5[0] + pila6[0] + pila7[0] + pila8[0] + pila9[0])
print("pila1: ", pila1)
print("pila2: ", pila2)
print("pila3: ", pila3)
print("pila4: ", pila4)
print("pila5: ", pila5)
print("pila6: ", pila6)
print("pila7: ", pila7)
print("pila8: ", pila8)
print("pila9: ", pila9)






fichero = open('datos.txt')
lista = []
for linea in fichero:
    lista.append(linea)
# print(lista)
finalizado = False
linea = 0
puntos = 0
items_1 = []
items_2 = []
condicion = False
movimientos = []


#     [V] [G]             [H]        
# [Z] [H] [Z]         [T] [S]        
# [P] [D] [F]         [B] [V] [Q]    
# [B] [M] [V] [N]     [F] [D] [N]    
# [Q] [Q] [D] [F]     [Z] [Z] [P] [M]
# [M] [Z] [R] [D] [Q] [V] [T] [F] [R]
# [D] [L] [H] [G] [F] [Q] [M] [G] [W]
# [N] [C] [Q] [H] [N] [D] [Q] [M] [B]
#  1   2   3   4   5   6   7   8   9 

#move 3 from 2 to 5
#mover 3 cajas de la pila 2 a la pila 5
#se muebve lo que está arriba del todo es decir primer elemento de la pila
for i in range (1, 10):
    locals()["pila"+str(i)] = []

while not finalizado:
    try:
        
    #lista[linea] = lista[linea].split() 
        pos = 0
        if lista[linea].split() != []:
            print(lista[linea])
            print(len(lista[linea]))
            print(lista[linea].split())

            if (lista[linea].split()[0] != 'move' and lista[linea].split()[0] != '1'):
                for char in lista[linea]:
                    if str(char) != ' ':
                        if pos%2 != 0:
                            print(char)
                            if pos == 1:
                                pila1.append(char)
                            elif pos == 5:
                                pila2.append(char)
                            elif pos == 9:
                                pila3.append(char)
                            elif pos == 13:
                                pila4.append(char)
                            elif pos == 17:
                                pila5.append(char)
                            elif pos == 21:
                                pila6.append(char)
                            elif pos == 25:
                                pila7.append(char)
                            elif pos == 29:
                                pila8.append(char)
                            elif pos == 33:
                                pila9.append(char)
                    pos+=1
            else:
                if lista[linea].split()[0] == 'move':
                    x = lista[linea].split()[3]
                    y = lista[linea].split()[5]
                    lista_aux = []
                    for i in range(1, int(lista[linea].split()[1]) + 1):

                        lista_aux.append(locals()["pila"+str(x)][0])
                        locals()["pila"+str(x)].pop(0)
                    for i in range(0, len(lista_aux)):
                        locals()["pila"+str(y)].insert(i, lista_aux[0])
                        lista_aux.pop(0)
                 

        linea+=1
    except:
        finalizado = True


print(movimientos)
print(pila1[0] + pila2[0] + pila3[0] + pila4[0] + pila5[0] + pila6[0] + pila7[0] + pila8[0] + pila9[0])
print("pila1: ", pila1)
print("pila2: ", pila2)
print("pila3: ", pila3)
print("pila4: ", pila4)
print("pila5: ", pila5)
print("pila6: ", pila6)
print("pila7: ", pila7)
print("pila8: ", pila8)
print("pila9: ", pila9)

