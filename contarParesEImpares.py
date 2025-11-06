quantidadeDeNumeros = int(input("Digite a quantidade de números, para digitar e assim ver quantos pares e ímpares digitou: "))
pares = 0
impares = 0


for i in range(0, quantidadeDeNumeros):
    numero = int(input("Digite um número: "))
    if (numero % 2 == 0):
        pares += 1 
    else:    
        impares += 1 

print("\n")
print("Quantidade de números pares: ", pares)
print("Quantidade de números ímpares: ", impares)