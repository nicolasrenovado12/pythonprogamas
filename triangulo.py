lado1 = int(input("Digite o lado1: "))
lado2 = int(input("Digite o lado2: "))
lado3 = int(input("Digite o lado3: "))


if (lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado3 + lado2 > lado1):
    print("É um triângulo")
    if (lado1 == lado2 and lado1 == lado3):
        print("Triângulo equilátero")
    elif (lado1 == lado2 or lado1 == lado3):
        print("Triângulo isósceles")
    elif (lado1 != lado2 and lado1 != lado3):
        print("Triângulo escaleno")
else:
    print("Não é um triângulo")