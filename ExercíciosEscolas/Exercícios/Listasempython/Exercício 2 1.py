lista = []

for i in range(0, 10, 1):
    
    print("Digite o número:", i+1)
    add = int(input(" "))
    lista.append(add)


lista.sort()
print("Menor elemento: ", lista[0], "\nMaior elemento: ", lista[9])

    
