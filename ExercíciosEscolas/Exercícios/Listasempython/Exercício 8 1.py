lista = []

for i in range(0, 5, 1):
    
    print("Digite o número:", i+1)
    add = int(input(" "))
    lista.append(add)

novalista = lista[4]
lista[4] = lista[0]
lista[0] = novalista


print(lista)

    
