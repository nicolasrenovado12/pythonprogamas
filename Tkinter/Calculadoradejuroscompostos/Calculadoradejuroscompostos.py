from tkinter import *
import os

def validate(value):

    try:
        if value:
     
            return int(value)
    except:
        return None



window = Tk()
Label(window, text="Digite quanto dinheiro quer colocar").pack()
dinheiroe = Entry(window)
dinheiroe.pack()
Label(window, text="Digite quantos meses/anos").pack()
mesese = Entry(window)
mesese.pack()

anual = IntVar()
Checkbutton(window, text="Anual", height=3,variable=anual).pack()
mensal = IntVar()
Checkbutton(window, text="Mensal", height=3,variable=mensal).pack()

Label(window, text="Porcentagem mensal", width=20).pack()
porcentagemmensale = Entry(window)
porcentagemmensale.pack()

simounao = IntVar()
Checkbutton(window, text="Irá colocar dinheiro durante os meses", height=3, variable=simounao).pack()


Label(window, text="Se sim quanto dinheiro irá colocar mensalmente?").pack()
dinheiromensale = Entry(window, )
dinheiromensale.pack()

def enviar():
    porcentagemmensal = validate(porcentagemmensale.get())
    dinheiro = validate(dinheiroe.get())
    meses = validate(mesese.get())
    aportemensal = validate(dinheiromensale.get())
    anos = meses * 12
    porcenmensal = (porcentagemmensal / 100) + 1
    
    if mensal.get() == 1 and anual.get() == 0:
        if simounao.get() == 1:
            print("sim")
            novovalor = dinheiro + (aportemensal * meses)
                
            print("Quanto colocou: ", novovalor)
                
            aportecompostos = aportemensal *(porcenmensal ** meses - 1) / (porcenmensal / 100)

                
            mesescompostos = dinheiro * (porcenmensal ** meses)
                
            montante = mesescompostos + aportecompostos
                
            juroscompostos = montante - novovalor
                
            print("Juros compostos: ", juroscompostos)
                
            print("Total: ", montante)
            
            
        else:
            
            print("O quanto colocou: ", dinheiro)
            montante = dinheiro * (porcenmensal ** meses)
            print("O seu montante será de ", montante)
            juroscompostos = montante - dinheiro
            print("O seu juros compostos será de ", juroscompostos)
    elif anual.get() == 1 and mensal.get() == 0:
        if simounao.get() == 1:
            print("")
            novovalor = dinheiro + (aportemensal * anos)
                
            print("Quanto colocou: ", novovalor)
                
            aportecompostos = aportemensal *(porcenmensal ** anos - 1) / (porcenmensal / 100)

                
            mesescompostos = dinheiro * (porcenmensal ** anos) 
                
            montante = mesescompostos + aportecompostos
                
            juroscompostos = montante - novovalor
                
            print("Juros compostos: ", juroscompostos)
                
            print("Total: ", montante)
        else:
            
            print("O quanto colocou: ", dinheiro)
            montante = dinheiro * (porcenmensal ** anos)
            print("O seu montante será de: ", montante)
            juroscompostos = montante - dinheiro
            print("O seu juros compostos será de: ", juroscompostos)
        
    elif anual.get() == 1 and mensal.get() == 1:
        print("Erro no progama")
    else:
        print("Erro no progama")


butao = Button(window, text="Enviar", command=enviar)
butao.pack()





window.mainloop()