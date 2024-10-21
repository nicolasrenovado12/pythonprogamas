print("Programa de ler um arquivo feito pelo usuario")

print("Digite a quantidade de numeros que preferir: \n")
listanumeros = []

for i in range(5):
    print("Fale o numero ", i+1)
    numero = int(input(""))
    listanumeros.append(numero)

with open("numeros.txt", "w") as arquivo:
    for i in listanumeros:
        arquivo.write(f"{i} " + '\n')


# Ler o arquivo
try:
    with open("numeros.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print("Numeros do arquivo:")
        print(conteudo)
except FileNotFoundError:
    print("O arquivo não foi encontrado")
     
print("Arquivo escrito, 'contatos.txt'")
