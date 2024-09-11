numerospares = 0
lista = []

for i in range(0, 15, 1):
    
    print("Digite o número:", i+1)
    add = int(input(" "))
    lista.append(add)

    if lista[i] % 2 == 0:
        numerospares +=1

print(numerospares)

    
