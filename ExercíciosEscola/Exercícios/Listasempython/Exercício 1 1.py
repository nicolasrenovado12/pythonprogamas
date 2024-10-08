lista = []

for i in range(0, 10, 1):
    print("Digite o número:", i+1)
    add = int(input(" "))
    lista.append(add)

sum = ((lista[0] + lista[9]) * 10) / 2
print(sum)

    
