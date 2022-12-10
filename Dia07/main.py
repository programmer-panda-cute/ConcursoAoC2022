fichero = open('datos.txt')
lista = []
for linea in fichero:
    lista.append(linea.rstrip('\n'))
finalizado = False
linea = 1
movimientos = []
comandos = []
respuestas = []
carpetas = []
directorios = [['/']]
pos_dir = -1
pos_index = 0
i = 0
root = []
txt = ""

nombre_carpetas = []

ubicacion = 0
ubicacion_anterior = 0
ubicacion_anterior2 = 0
ubicacion_anterior3 = 0
ubicacion_anterior4 = 0
carpeta_ub = "root/"


while not finalizado:
    try:
        if lista[linea].split()[1] == "cd" and lista[linea].split()[2] == "..":
            carpeta_ub = carpeta_ub.split("/")[0:-2]
            txt = ""
            for i in carpeta_ub:
                txt = txt + i + "/"
            carpeta_ub = txt
            txt = ""

            linea += 1

        elif lista[linea].split()[1] == "cd":
            carpeta_ub = carpeta_ub + lista[linea].split()[2] + "/"
            if carpeta_ub not in nombre_carpetas:
                locals()[carpeta_ub] = []
                nombre_carpetas.append(carpeta_ub)
            if [lista[linea].split()[2]] in locals()[carpeta_ub]:
                linea += 1
                if lista[linea].split()[1] == "ls":
                    linea += 1
                    while lista[linea].split()[0] != "$":
                        if lista[linea].split()[0] == "dir":
                            locals()[carpeta_ub].append([lista[linea].split()[1]])
                            locals()[carpeta_ub + lista[linea].split()[1] + "/"] = []
                            nombre_carpetas.append(carpeta_ub + lista[linea].split()[1] + "/")
                        else:
                            locals()[carpeta_ub].append(lista[linea])
                        linea+=1
            else:
                locals()[carpeta_ub].append([lista[linea].split()[2]])
                linea += 1
                if lista[linea].split()[1] == "ls":
                    linea += 1
                    while lista[linea].split()[0] != "$":
                        if lista[linea].split()[0] == "dir":
                            locals()[carpeta_ub].append([lista[linea].split()[1]])
                            locals()[carpeta_ub + lista[linea].split()[1] + "/"] = []
                            nombre_carpetas.append(carpeta_ub + lista[linea].split()[1] + "/")
                        else:
                            locals()[carpeta_ub].append(lista[linea])
                        linea+=1

        elif lista[linea].split()[1] == "ls":
            nombre_carpetas.append("root")
            linea += 1
            while lista[linea].split()[0] != "$":
                if lista[linea].split()[0] == "dir":
                    root.append([lista[linea].split()[1]])
                else:
                    root.append(lista[linea])
                linea+=1
    except:
        finalizado = True
nombre_carpetas.pop(0)

# print("nombre_carpetas",nombre_carpetas)

lista_nombre_carpetas = nombre_carpetas.copy()



for i in range (0, len (root)):
    if isinstance(root[i], list):
        if str("root/" + root[i][0] + "/") in nombre_carpetas:
            nombre_carpetas.remove(str("root/" + root[i][0] + "/"))
            root[i] = locals()[str("root/" + root[i][0] + "/")]

for i in range(0, len(root)):
    # try:
    if isinstance(root[i], list):
        for j in range(0, len(root[i])):
            if isinstance(root[i][j], list):
                if str("root/" + root[i][0][0] + "/" + root[i][j][0] + "/") in nombre_carpetas:
                    nombre_carpetas.remove(str("root/" + root[i][0][0] + "/" + root[i][j][0] + "/"))
                    root[i][j] = locals()[str("root/" + root[i][0][0] + "/" + root[i][j][0] + "/")]

    # except:
    #     pass


for i in range(0, len(root)):
    if isinstance(root[i], list):
        for j in range(0, len(root[i])):
            if isinstance(root[i][j], list):
                for k in range (0, len(root[i][j])):
                    if isinstance(root[i][j][k], list):
                        if str("root/" + root[i][0][0] + "/" + root[i][j][0][0] + "/" + root[i][j][k][0] + "/") in nombre_carpetas:
                            nombre_carpetas.remove(str("root/" + root[i][0][0] + "/" + root[i][j][0][0] + "/" + root[i][j][k][0] + "/"))
                            root[i][j][k] = locals()[str("root/" + root[i][0][0] + "/" + root[i][j][0][0] + "/" + root[i][j][k][0] + "/")]




for i in range(0, len(root)):
    if isinstance(root[i], list):
        for j in range(0, len(root[i])):
            if isinstance(root[i][j], list):
                for k in range (0, len(root[i][j])):
                    if isinstance(root[i][j][k], list):
                        print( root[i][j][k])
                        for l in range (0, len(root[i][j][k])):
                            if isinstance(root[i][j][k][l], list):
                                if l != 0:
                                    if str("root/" + root[i][0][0] + "/" + root[i][j][0][0] + "/" + root[i][j][k][0][0] + "/" + root[i][j][k][l][0] + "/") in nombre_carpetas:
                                        nombre_carpetas.remove(str("root/" + root[i][0][0] + "/" + root[i][j][0][0] + "/" + root[i][j][k][0][0] + "/" + root[i][j][k][l][0] + "/"))
                                        root[i][j][k][l] = locals()[str("root/" + root[i][0][0] + "/" + root[i][j][0][0] + "/" + root[i][j][k][0][0] + "/" + root[i][j][k][l][0] + "/")]


for i in range(0, len(root)):
    if isinstance(root[i], list):
        for j in range(0, len(root[i])):
            if isinstance(root[i][j], list):
                for k in range (0, len(root[i][j])):
                    if isinstance(root[i][j][k], list):
                        for l in range (0, len(root[i][j][k])):
                            if isinstance(root[i][j][k][l], list):
                                for t in range (0, len(root[i][j][k][l])):
                                    if isinstance(root[i][j][k][l][t], list):
                                        if t != 0:
                                            if str("root/" + root[i][0][0] + "/" + root[i][j][0][0] + "/" + root[i][j][k][0][0] + "/" + root[i][j][k][l][0][0] + "/" + root[i][j][k][l][t][0] + "/") in nombre_carpetas:
                                                nombre_carpetas.remove(str("root/" + root[i][0][0] + "/" + root[i][j][0][0] + "/" + root[i][j][k][0][0] + "/" + root[i][j][k][l][0][0] + "/" + root[i][j][k][l][t][0] + "/"))
                                                root[i][j][k][l][t] = locals()[str("root/" + root[i][0][0] + "/" + root[i][j][0][0] + "/" + root[i][j][k][0][0] + "/" + root[i][j][k][l][0][0] + "/" + root[i][j][k][l][t][0] + "/")]


for i in range(0, len(root)):
    if isinstance(root[i], list):
        for j in range(0, len(root[i])):
            if isinstance(root[i][j], list):
                for k in range (0, len(root[i][j])):
                    if isinstance(root[i][j][k], list):
                        for l in range (0, len(root[i][j][k])):
                            if isinstance(root[i][j][k][l], list):
                                for t in range (0, len(root[i][j][k][l])):
                                    if isinstance(root[i][j][k][l][t], list):
                                        for m in range (0, len(root[i][j][k][l][t])):
                                            if isinstance(root[i][j][k][l][t][m], list):
                                                if m != 0:
                                                    if str("root/" + root[i][0][0] + "/" + root[i][j][0][0] + "/" + root[i][j][k][0][0] + "/" + root[i][j][k][l][0][0] + "/" + root[i][j][k][l][t][0][0] + "/" + root[i][j][k][l][t][m][0] + "/") in nombre_carpetas:
                                                        nombre_carpetas.remove(str("root/" + root[i][0][0] + "/" + root[i][j][0][0] + "/" + root[i][j][k][0][0] + "/" + root[i][j][k][l][0][0] + "/" + root[i][j][k][l][t][0][0] + "/" + root[i][j][k][l][t][m][0] + "/"))
                                                        root[i][j][k][l][t][m] = locals()[str("root/" + root[i][0][0] + "/" + root[i][j][0][0] + "/" + root[i][j][k][0][0] + "/" + root[i][j][k][l][0][0] + "/" + root[i][j][k][l][t][0][0] + "/" + root[i][j][k][l][t][m][0] + "/")]


for i in range(0, len(root)):
    if isinstance(root[i], list):
        for j in range(0, len(root[i])):
            if isinstance(root[i][j], list):
                for k in range (0, len(root[i][j])):
                    if isinstance(root[i][j][k], list):
                        for l in range (0, len(root[i][j][k])):
                            if isinstance(root[i][j][k][l], list):
                                for t in range (0, len(root[i][j][k][l])):
                                    if isinstance(root[i][j][k][l][t], list):
                                        for m in range (0, len(root[i][j][k][l][t])):
                                            if isinstance(root[i][j][k][l][t][m], list):
                                                for n in range (0, len(root[i][j][k][l][t][m])):
                                                    if isinstance(root[i][j][k][l][t][m][n], list):
                                                        if n != 0:
                                                            if str("root/" + root[i][0][0] + "/" + root[i][j][0][0] + "/" + root[i][j][k][0][0] + "/" + root[i][j][k][l][0][0] + "/" + root[i][j][k][l][t][0][0] + "/" + root[i][j][k][l][t][m][0][0] + "/" + root[i][j][k][l][t][m][n][0] + "/") in nombre_carpetas:
                                                                nombre_carpetas.remove(str("root/" + root[i][0][0] + "/" + root[i][j][0][0] + "/" + root[i][j][k][0][0] + "/" + root[i][j][k][l][0][0] + "/" + root[i][j][k][l][t][0][0] + "/" + root[i][j][k][l][t][m][0][0] + "/" + root[i][j][k][l][t][m][n][0] + "/"))
                                                                root[i][j][k][l][t][m][n] = locals()[str("root/" + root[i][0][0] + "/" + root[i][j][0][0] + "/" + root[i][j][k][0][0] + "/" + root[i][j][k][l][0][0] + "/" + root[i][j][k][l][t][0][0] + "/" + root[i][j][k][l][t][m][0][0] + "/" + root[i][j][k][l][t][m][n][0] + "/")]


for i in range(0, len(root)):
    if isinstance(root[i], list):
        for j in range(0, len(root[i])):
            if isinstance(root[i][j], list):
                for k in range (0, len(root[i][j])):
                    if isinstance(root[i][j][k], list):
                        for l in range (0, len(root[i][j][k])):
                            if isinstance(root[i][j][k][l], list):
                                for t in range (0, len(root[i][j][k][l])):
                                    if isinstance(root[i][j][k][l][t], list):
                                        for m in range (0, len(root[i][j][k][l][t])):
                                            if isinstance(root[i][j][k][l][t][m], list):
                                                for n in range (0, len(root[i][j][k][l][t][m])):
                                                    if isinstance(root[i][j][k][l][t][m][n], list):
                                                        for o in range (0, len(root[i][j][k][l][t][m][n])):
                                                            if isinstance(root[i][j][k][l][t][m][n][o], list):
                                                                if o != 0:
                                                                    if str("root/" + root[i][0][0] + "/" + root[i][j][0][0] + "/" + root[i][j][k][0][0] + "/" + root[i][j][k][l][0][0] + "/" + root[i][j][k][l][t][0][0] + "/" + root[i][j][k][l][t][m][0][0] + "/" + root[i][j][k][l][t][m][n][0][0] + "/" + root[i][j][k][l][t][m][n][o][0] + "/") in nombre_carpetas:
                                                                        nombre_carpetas.remove(str("root/" + root[i][0][0] + "/" + root[i][j][0][0] + "/" + root[i][j][k][0][0] + "/" + root[i][j][k][l][0][0] + "/" + root[i][j][k][l][t][0][0] + "/" + root[i][j][k][l][t][m][0][0] + "/" + root[i][j][k][l][t][m][n][0][0] + "/" + root[i][j][k][l][t][m][n][o][0] + "/"))
                                                                        root[i][j][k][l][t][m][n][o] = locals()[str("root/" + root[i][0][0] + "/" + root[i][j][0][0] + "/" + root[i][j][k][0][0] + "/" + root[i][j][k][l][0][0] + "/" + root[i][j][k][l][t][0][0] + "/" + root[i][j][k][l][t][m][0][0] + "/" + root[i][j][k][l][t][m][n][0][0] + "/" + root[i][j][k][l][t][m][n][o][0] + "/")]


for i in range(0, len(root)):
    if isinstance(root[i], list):
        for j in range(0, len(root[i])):
            if isinstance(root[i][j], list):
                for k in range (0, len(root[i][j])):
                    if isinstance(root[i][j][k], list):
                        for l in range (0, len(root[i][j][k])):
                            if isinstance(root[i][j][k][l], list):
                                for t in range (0, len(root[i][j][k][l])):
                                    if isinstance(root[i][j][k][l][t], list):
                                        for m in range (0, len(root[i][j][k][l][t])):
                                            if isinstance(root[i][j][k][l][t][m], list):
                                                for n in range (0, len(root[i][j][k][l][t][m])):
                                                    if isinstance(root[i][j][k][l][t][m][n], list):
                                                        for o in range (0, len(root[i][j][k][l][t][m][n])):
                                                            if isinstance(root[i][j][k][l][t][m][n][o], list):
                                                                for p in range (0, len(root[i][j][k][l][t][m][n][o])):
                                                                    if isinstance(root[i][j][k][l][t][m][n][o][p], list):
                                                                        if p != 0:
                                                                            if str("root/" + root[i][0][0] + "/" + root[i][j][0][0] + "/" + root[i][j][k][0][0] + "/" + root[i][j][k][l][0][0] + "/" + root[i][j][k][l][t][0][0] + "/" + root[i][j][k][l][t][m][0][0] + "/" + root[i][j][k][l][t][m][n][0][0] + "/" + root[i][j][k][l][t][m][n][o][0][0] + "/" + root[i][j][k][l][t][m][n][o][p][0] + "/") in nombre_carpetas:
                                                                                nombre_carpetas.remove(str("root/" + root[i][0][0] + "/" + root[i][j][0][0] + "/" + root[i][j][k][0][0] + "/" + root[i][j][k][l][0][0] + "/" + root[i][j][k][l][t][0][0] + "/" + root[i][j][k][l][t][m][0][0] + "/" + root[i][j][k][l][t][m][n][0][0] + "/" + root[i][j][k][l][t][m][n][o][0][0] + "/" + root[i][j][k][l][t][m][n][o][p][0] + "/"))
                                                                                root[i][j][k][l][t][m][n][o][p] = locals()[str("root/" + root[i][0][0] + "/" + root[i][j][0][0] + "/" + root[i][j][k][0][0] + "/" + root[i][j][k][l][0][0] + "/" + root[i][j][k][l][t][0][0] + "/" + root[i][j][k][l][t][m][0][0] + "/" + root[i][j][k][l][t][m][n][0][0] + "/" + root[i][j][k][l][t][m][n][o][0][0] + "/" + root[i][j][k][l][t][m][n][o][p][0] + "/")]
                                                                                




print("imprimiendo root")
for i in root:
    if isinstance(i, list):
        print(i[0])
        for j in i[1:]:
            if isinstance(j, list):
                for k in j[1:]:
                    if isinstance(k, list):
                        print("\t\t" + k[0][0] + "(dir)")
                        for l in k[1:]:
                            if isinstance(l, list):
                                print("\t\t\t" + l[0][0] + "(dir)")
                                for m in l[1:]:
                                    if isinstance(m, list):
                                        print("\t\t\t\t" + m[0][0] + "(dir)")
                                        for n in m[1:]:
                                            if isinstance(n, list):
                                                print("\t\t\t\t\t" + n[0][0] + "(dir)")
                                                for o in n[1:]:
                                                    if isinstance(o, list):
                                                        print("\t\t\t\t\t\t" + o[0][0] + "(dir)")
                                                        for p in o[1:]:
                                                            if isinstance(p, list):
                                                                print("\t\t\t\t\t\t\t" + p[0][0] + "(dir)")
                                                                for q in p[1:]:
                                                                    if isinstance(q, list):
                                                                        print("\t\t\t\t\t\t\t\t" + q[0][0] + "(dir)")
                                                                        for r in q[1:]:
                                                                            if isinstance(r, list):
                                                                                print("\t\t\t\t\t\t\t\t\t" + r[0][0] + "(dir)")
                                                                                for s in r[1:]:
                                                                                    if isinstance(s, list):
                                                                                        print("\t\t\t\t\t\t\t\t\t\t" + s[0][0] + "(dir)")
                                                                                        print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
                                                                                    else:
                                                                                        print("\t\t\t\t\t\t\t\t\t\t" + s)
                                                                            else:
                                                                                print("\t\t\t\t\t\t\t\t\t" + r)
                                                                    else:
                                                                        print("\t\t\t\t\t\t\t\t" + q)
                                                            else:
                                                                print("\t\t\t\t\t\t\t" + p)
                                                    else:
                                                        print("\t\t\t\t\t\t" + o)
                                            else:
                                                print("\t\t\t\t\t" + n)

                                    else:
                                        print("\t\t\t\t" + m)
                            else:
                                print("\t\t\t" + l)
                    else:
                        print("\t\t" + k)
            else:
                print("\t" + j)

    else:
        print(i)

for i in lista_nombre_carpetas:
    ubicación = i.split("/")
    ubicación = ubicación[1:-1]
    ubicacion = len(ubicación)
    if ubicacion == 1:
        for aux in root:
            if isinstance(aux, list):
                if ubicación[0] == aux[0][0]:
                    locals()[i + "peso"] = aux
    elif ubicacion == 2:
        print("ubicación", ubicación)
        for aux in root:
            if isinstance(aux, list):
                if ubicación[0] == aux[0][0]:
                    for j in aux:
                        if isinstance(j, list):
                            if ubicación[1] == j[0][0]:
                                locals()[i + "peso"] = j
    
    elif ubicacion == 3:
        for aux in root:
            if isinstance(aux, list):
                if ubicación[0] == aux[0][0]:
                    for j in aux:
                        if isinstance(j, list):
                            if ubicación[1] == j[0][0]:
                                for k in j:
                                    if isinstance(k, list):
                                        if ubicación[2] == k[0][0]:
                                            locals()[i + "peso"] = k
    elif ubicacion == 4:
        for aux in root:
            if isinstance(aux, list):
                if ubicación[0] == aux[0][0]:
                    for j in aux:
                        if isinstance(j, list):
                            if ubicación[1] == j[0][0]:
                                for k in j:
                                    if isinstance(k, list):
                                        if ubicación[2] == k[0][0]:
                                            for l in k:
                                                if isinstance(l, list):
                                                    if ubicación[3] == l[0][0]:
                                                        locals()[i + "peso"] = l
    elif ubicacion == 5:
        for aux in root:
            if isinstance(aux, list):
                if ubicación[0] == aux[0][0]:
                    for j in aux:
                        if isinstance(j, list):
                            if ubicación[1] == j[0][0]:
                                for k in j:
                                    if isinstance(k, list):
                                        if ubicación[2] == k[0][0]:
                                            for l in k:
                                                if isinstance(l, list):
                                                    if ubicación[3] == l[0][0]:
                                                        for m in l:
                                                            if isinstance(m, list):
                                                                if ubicación[4] == m[0][0]:
                                                                    locals()[i + "peso"] = m
    elif ubicacion == 6:
        for aux in root:
            if isinstance(aux, list):
                if ubicación[0] == aux[0][0]:
                    for j in aux:
                        if isinstance(j, list):
                            if ubicación[1] == j[0][0]:
                                for k in j:
                                    if isinstance(k, list):
                                        if ubicación[2] == k[0][0]:
                                            for l in k:
                                                if isinstance(l, list):
                                                    if ubicación[3] == l[0][0]:
                                                        for m in l:
                                                            if isinstance(m, list):
                                                                if ubicación[4] == m[0][0]:
                                                                    for n in m:
                                                                        if isinstance(n, list):
                                                                            if ubicación[5] == n[0][0]:
                                                                                locals()[i + "peso"] = n
    elif ubicacion == 7:
        for aux in root:
            if isinstance(aux, list):
                if ubicación[0] == aux[0][0]:
                    for j in aux:
                        if isinstance(j, list):
                            if ubicación[1] == j[0][0]:
                                for k in j:
                                    if isinstance(k, list):
                                        if ubicación[2] == k[0][0]:
                                            for l in k:
                                                if isinstance(l, list):
                                                    if ubicación[3] == l[0][0]:
                                                        for m in l:
                                                            if isinstance(m, list):
                                                                if ubicación[4] == m[0][0]:
                                                                    for n in m:
                                                                        if isinstance(n, list):
                                                                            if ubicación[5] == n[0][0]:
                                                                                for o in n:
                                                                                    if isinstance(o, list):
                                                                                        if ubicación[6] == o[0][0]:
                                                                                            locals()[i + "peso"] = o
    elif ubicacion == 8:
        for aux in root:
            if isinstance(aux, list):
                if ubicación[0] == aux[0][0]:
                    for j in aux:
                        if isinstance(j, list):
                            if ubicación[1] == j[0][0]:
                                for k in j:
                                    if isinstance(k, list):
                                        if ubicación[2] == k[0][0]:
                                            for l in k:
                                                if isinstance(l, list):
                                                    if ubicación[3] == l[0][0]:
                                                        for m in l:
                                                            if isinstance(m, list):
                                                                if ubicación[4] == m[0][0]:
                                                                    for n in m:
                                                                        if isinstance(n, list):
                                                                            if ubicación[5] == n[0][0]:
                                                                                for o in n:
                                                                                    if isinstance(o, list):
                                                                                        if ubicación[6] == o[0][0]:
                                                                                            for p in o:
                                                                                                if isinstance(p, list):
                                                                                                    if ubicación[7] == p[0][0]:
                                                                                                        locals()[i + "peso"] = p
    elif ubicacion == 9:
        for aux in root:
            if isinstance(aux, list):
                if ubicación[0] == aux[0][0]:
                    for j in aux:
                        if isinstance(j, list):
                            if ubicación[1] == j[0][0]:
                                for k in j:
                                    if isinstance(k, list):
                                        if ubicación[2] == k[0][0]:
                                            for l in k:
                                                if isinstance(l, list):
                                                    if ubicación[3] == l[0][0]:
                                                        for m in l:
                                                            if isinstance(m, list):
                                                                if ubicación[4] == m[0][0]:
                                                                    for n in m:
                                                                        if isinstance(n, list):
                                                                            if ubicación[5] == n[0][0]:
                                                                                for o in n:
                                                                                    if isinstance(o, list):
                                                                                        if ubicación[6] == o[0][0]:
                                                                                            for p in o:
                                                                                                if isinstance(p, list):
                                                                                                    if ubicación[7] == p[0][0]:
                                                                                                        for q in p:
                                                                                                            if isinstance(q, list):
                                                                                                                if ubicación[8] == q[0][0]:
                                                                                                                    locals()[i + "peso"] = q
    elif ubicacion == 10:
        for aux in root:
            if isinstance(aux, list):
                if ubicación[0] == aux[0][0]:
                    for j in aux:
                        if isinstance(j, list):
                            if ubicación[1] == j[0][0]:
                                for k in j:
                                    if isinstance(k, list):
                                        if ubicación[2] == k[0][0]:
                                            for l in k:
                                                if isinstance(l, list):
                                                    if ubicación[3] == l[0][0]:
                                                        for m in l:
                                                            if isinstance(m, list):
                                                                if ubicación[4] == m[0][0]:
                                                                    for n in m:
                                                                        if isinstance(n, list):
                                                                            if ubicación[5] == n[0][0]:
                                                                                for o in n:
                                                                                    if isinstance(o, list):
                                                                                        if ubicación[6] == o[0][0]:
                                                                                            for p in o:
                                                                                                if isinstance(p, list):
                                                                                                    if ubicación[7] == p[0][0]:
                                                                                                        for q in p:
                                                                                                            if isinstance(q, list):
                                                                                                                if ubicación[8] == q[0][0]:
                                                                                                                    for r in q:
                                                                                                                        if isinstance(r, list):
                                                                                                                            if ubicación[9] == r[0][0]:
                                                                                                                                locals()[i + "peso"] = r
    else:
        print("...................................................................................")



for i in lista_nombre_carpetas:
    peso = 0
    if isinstance(locals()[i + "peso"], list):
        for j in locals()[i + "peso"]:
            if isinstance(j, list):
                for k in j:
                    if isinstance(k, list):
                        for l in k:
                            if isinstance(l, list):
                                for m in l:
                                    if isinstance(m, list):
                                        for n in m:
                                            if isinstance(n, list):
                                                for o in n:
                                                    if isinstance(o, list):
                                                        for p in o:
                                                            if isinstance(p, list):
                                                                for q in p:
                                                                    if isinstance(q, list):
                                                                        for r in q:
                                                                            if isinstance(r, list):
                                                                                for s in r:
                                                                                    if isinstance(s, list):
                                                                                        print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
                                                                                    else:
                                                                                        if s.split()[0].isdigit():
                                                                                            peso += int(s.split()[0])

                                                                            else:
                                                                                if r.split()[0].isdigit():
                                                                                    peso += int(r.split()[0])
                                                                    else:
                                                                        if q.split()[0].isdigit():
                                                                            peso += int(q.split()[0])
                                                            else:
                                                                if p.split()[0].isdigit():
                                                                    peso += int(p.split()[0])
                                                    else:
                                                        if o.split()[0].isdigit():
                                                            peso += int(o.split()[0])
                                                        else:
                                                            print("O", o.split()[0])
                                                                            
                                            else:
                                                if n.split()[0].isdigit():
                                                    peso += int(n.split()[0])
                                    else:
                                        if m.split()[0].isdigit():
                                            peso += int(m.split()[0])
                            else:
                                if l.split()[0].isdigit():
                                    peso += int(l.split()[0])
                    else:
                        if k.split()[0].isdigit():
                            peso += int(k.split()[0])
            else:
                if j.split()[0].isdigit():
                    peso += int(j.split()[0])
    else:
        peso += int(locals()[i + "peso"].split()[0])
    locals()[i + "peso"] = peso

peso_resultado = 0
for i in lista_nombre_carpetas:
    if locals()[i + "peso"] < 100000:
        peso_resultado += locals()[i + "peso"]
    print(i + "peso", locals()[i + "peso"])

print("peso_resultado", peso_resultado)

# for i in range(0, len(root)):
#     try:
#         if isinstance(root[i], list):
#             print("root[i][0][0]",root[i][0][0])
#             for j in range(0, len(root[i])):
#                 if str("root/" + root[i][0][0] + "/" + root[i][j][0] + "/") in nombre_carpetas:
#                     print(str("root/" + root[i][0][0] + "/" + root[i][j][0] + "/"))
#                     root[i][j] = locals()[str("root/" + root[i][0][0] + "/" + root[i][j][0] + "/")]
#                     nombre_carpetas.remove(str("root/" + root[i][0][0] + "/" + root[i][j][0] + "/"))

#     except:
#         pass

peso_total = 0
for i in lista_nombre_carpetas:
    u = i.split("/")
    if len(u) == 3:
        print(u)
        print("---------")
        peso_total += locals()[i + "peso"]
        print("i", locals()[i + "peso"])

print("peso_total", peso_total)
espacio_necesario = 70000000 - peso_total - 30000000
print("El espacio necesario es de " + str(70000000 - peso_total - 30000000 ) + " bytes")

lista_w = []
for i in lista_nombre_carpetas:
    if int(locals()[i + "peso"]) >= abs(espacio_necesario):
        lista_w.append(int(locals()[i + "peso"]))

print(min(lista_w))


# for i in range (0, len (root)):
#     if type(root[i]) == list:
#         if str("root/" + root[i][0] + "/") in nombre_carpetas:
#             print(str("root/" + root[i][0] + "/"))
#             root[i] = locals()[str("root/" + root[i][0] + "/")]
#             nombre_carpetas.remove(str("root/" + root[i][0][0] + "/"))
        

# print("root",root)



# for i in range (0, len (root)):


# locals()["rootw"] = 
# for i in nombre_carpetas:
#     print(i, locals()[i])







# for i in nombre_carpetas:

#     print(i.split("/"))
#     # if i.split("/")[-2] in locals()[i]:
#     #     print(i.split("/")[-2])
#         #locals()[i].remove(i.split("/")[-2])



# while len(nombre_carpetas) > 0:
#     for i in nombre_carpetas:
#         if i in root:
#             root[root.index(i)] = locals()[i]
#             nombre_carpetas.remove(i)
    
# print("nombre_carpetas",nombre_carpetas)


