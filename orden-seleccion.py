def selection(lista):
    for i in range (len(lista)):
        for j in range (i, (len(lista))):
            if lista [j] < lista [i]:
                lista [i], lista [j] = lista [j], lista [i]
    return lista

list = [8,2,5,6]
print (selection(list))
