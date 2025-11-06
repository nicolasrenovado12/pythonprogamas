print("[1] Converter Celsius para Fahrenheit \n" +
       "[2] Converter Fahrenheit para Celsius \n" +
       "[3] Converter Celsius para Kelvin \n" + 
       "[4] Converter Metros para Milhas \n" +
       "[5] Converter Centímetros para Polegadas \n" +
       "[6] Converter Valores em Real para Dólar \n" +
       "[7] Converter Quilos para Gramas \n" +
       "[8] Converter Litros para Mililitros \n" +
       "[0] Sair \n")

selecionarCaso = int(input("Qual caso você quer? "))

match selecionarCaso:
    case 0: 
        print("O programa acabou. ")

    case 1:
        grausCelsius = int(input("Digite os graus celsius: "))
        farenheit = (grausCelsius * 9/5) + 32
        print("Graus para farenheit:", farenheit)

    case 2:
        farenheit = int(input("Digite farenheit: "))
        grausCelsius = (farenheit - 32) * 5/9
        print("Farenheit para graus:", grausCelsius)

    case 3:
        grausCelsius = int(input("Digite os graus celsius: "))
        kelvin = grausCelsius + 273.15
        print("Graus para kelvin:", kelvin)

    case 4: 
        metros = int(input("Digite metros: "))
        milhas = metros / 1609
        print("Metros para milhas:", milhas)

    case 5:
        centimetros = int(input("Digite centímetros: "))
        polegadas = centimetros / 2.54
        print("Centímetros para polegadas:", polegadas)

    case 6:
        real = int(input("Digite real: "))
        dolar = real * 5.36
        print("Real para dolar:", dolar)

    case 7:
        quilos = int(input("Digite quilos: "))
        gramas = quilos * 1000
        print("Quilos para gramas:", gramas)

    case 8:
        litros = int(input("Digite quilos: "))
        mililitros = litros * 1000
        print("Litros para mililitros:", mililitros)

