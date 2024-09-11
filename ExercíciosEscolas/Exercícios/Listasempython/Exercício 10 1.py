lista1 = []
lista2 = []
novalista = []
for i in range(0, 5, 1):
    
    print("Digite o número:", i+1, "da lista 2 ")
    add = int(input(" "))
    lista1.append(add)
for i in range(0, 5, 1):
    
    print("Digite o número:", i+1, "da lista 2 ")
    add = int(input(" "))
    lista2.append(add)


for i in range(0, 5, 1):
    produto = lista1[i] * lista2[i]
    novalista.append(produto)

print(novalista)

    
