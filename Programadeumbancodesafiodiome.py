saques = 0
depositos = 0
saldo = 0
limite = 500
numeros_saques = 0
numeros_depositos = 0

while True:

    text = int(input("Este é um sistema bancario de deposito e saque.\nO maximo de depositos que pode fazer é 3, e pode apenas sacar 3 vezes ao dia, \no progama é realizado em numeros. O que quer fazer? SAIR[0] SACAR[1] DEPOSITAR[2] VER EXTRATO[3] "))
    
    
    if text == 0:
        print("O progama terminou")
        break
    elif text == 1:
 
        sacar = float(input("Digite o quanto quer sacar: \n"))
        
        if saldo <= 0:
            print("Não há o que sacar")
        elif 3 <= numeros_saques:
            print("Excedeu a os seus saques diarios\n")
        elif sacar < 0:
            print("Não da para sacar com numero negativos\n")
        else:
            
            saldo -= sacar
            saques += sacar
            print("Saque realizado. Saldo restante: ", saldo, "\n")
            numeros_saques += 1
            
        
    elif text == 2:
        
        depositar = int(input("Digite o quanto quer depositar: \n"))
        
        saldo += depositar
        depositos += depositar
        
        print("Este foi o saldo depois do deposito:", saldo)
        numeros_depositos += 1
        
    elif text == 3:
        if numeros_saques == 0 and numeros_depositos == 0:
            print("Não há extrato. ")
        else: 
            print("ESTE FOI O SEU EXTRATO: \n")
            print("NUMERO DE SAQUES: ", numeros_saques, "\n")
            print("NUMERO DE DEPOSITOS: ", numeros_depositos, "\n")  
            
            print("DINHEIRO SACADOS: R$%s.00" % (saques), "\n")
            print("DINHEIRO DEPOSITADOS: R$%s.00" % (depositos), "\n")  
           
            
            
        
 

   
    
    
    
    
    
    