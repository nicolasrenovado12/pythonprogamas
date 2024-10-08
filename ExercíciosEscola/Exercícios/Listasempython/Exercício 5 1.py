lista1 = []
lista2 = []

for i in range(0, 5, 1):
    
    print("Digite o número:", i+1, "da lista 1 ")
    add = int(input(" "))
    lista1.append(add)
for i in range(0, 5, 1):
    
    print("Digite o número:", i+1, "da lista 2 ")
    add = int(input(" "))
    lista2.append(add)

intersecção = list(set(lista1) & set(lista2))
print(intersecção)

    
