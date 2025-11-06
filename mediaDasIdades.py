media = 0
soma = 0 
quantidade = 0
idade = 1 # Apenas um exemplo

print("O programa fará a média de todas as idades: ")
while (idade != 0):
    idade = int(input("Digite uma idade: "))
    if (idade != 0):
        soma+=idade
        quantidade+=1

media = soma / quantidade

print("Média de todas as idades: " , media)
