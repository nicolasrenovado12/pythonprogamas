ano = int(input("Digite um ano: "))
ultimos2AlgarismosAno = ano % 100

if (ultimos2AlgarismosAno % 4 == 0):
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")