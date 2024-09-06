lista = []
for i in range(0, 10, 1):
    print("Digite o número:", i+1)
    add = int(input(" "))
    lista.append(add)

novalista = [lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8], lista[9]]
a = 9
print("Sem reverter: ", lista)
for i in range(0, 10, 1):
    lista[i] = novalista[a]
    a-=1
    if i == 9:
        print("Revertida: ", lista)


# Consegui fazer uma lista revertida, sem a necessidade de .reverse.