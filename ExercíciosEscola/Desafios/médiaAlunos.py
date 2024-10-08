

quantosalunos = int(input("Quantos alunos?"))
Nomesdosalunos = []
nota1bimestre = []
nota2bimestre = []
média = []
i = 0 
for i in range(0, quantosalunos, 1):
    situação = []
    print("Coloque o nome do aluno ", i + 1)
    nome=input("")
    Nomesdosalunos.append(nome)

    
    nota1 = input("Qual a nota do aluno do primeiro bimestre? ")
    nota2 = input("Qual a nota do aluno do segundo bimestre? ")
    nota1bimestre.append(nota1)
    nota2bimestre.append(nota2)
    


    média.append((float(nota1) + float(nota2)) / 2)
    médiaaprovadoounao = (float(nota1) + float(nota2)) / 2
    print(" Nota 1 bimestre ", nota1, "\n", "Nota 2 bimestre:", nota2, "\n", "média: ", média[i])
    if médiaaprovadoounao >= 7:
        print(Nomesdosalunos[i], "Foi aprovado")
    else:
        print(Nomesdosalunos[i], "Foi reprovado")


escolha = int(input("você quer ver qual aluno (digite em numero)"))
print("Nome do aluno: ", Nomesdosalunos[escolha], "    Média deste aluno: ", média[escolha])
if média[escolha] >= 7:
    print("Com esta média, este aluno foi aprovado. ")
else:
    print("Com esta média, este aluno foi reprovado")