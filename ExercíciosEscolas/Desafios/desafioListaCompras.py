print("Programa para a manipulação de lista de mercado: ")
b=0
Lista = []

def mostrarnumero(): 
    quantidade = len(Lista)
    for n in range(0, quantidade, 1):
        print(n+1, ".", Lista[n])


for i in range(0, 5, 1):
    print("Digite a compra", i+1)
    compra = input("")
    Lista.append(compra)  

print("Assim ficou a sua lista: ")
mostrarnumero()


while (b == 0):

    remocao = input("Deseja remover algum numero? s/n ")
    adicao = input("Deseja adicionar algum numero? s/n ")


    if (remocao == "s"):
        opcao = input("Qual item deseja excluir? ")
        
        print("O item", opcao, "foi removido da lista.")
        Lista.remove(opcao)
    else:
        b+=1

    if (adicao == "s"):
        opcao2 = input("O que quer adicionar? ")

        Lista.insert(1, opcao2)

Lista.sort()
mostrarnumero()

print("A lista foi realizada. Os nomes estão em ordem alfabética.  ")

