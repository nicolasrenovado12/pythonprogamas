from random import randrange

    
def Computador():
    ocupiedrows = []
    ocupiedcolumns = []
    
    for i in range(10):
            ok = True
    while ok:
        print("-------- -------- --------\n ")
        print("Os jogos são por números digite o seu número para começar ")
        entrada = int(input(""))
        row = entrada -1
        if row / 3 < 1:
            column = 0
        elif row / 3 < 2:
            column = 1
        else:
            column = 2
        
        ocupiedrows.append(row)
        ocupiedcolumns.append(column)
        print(ocupiedrows)
        print(ocupiedcolumns)
        condicoesvitoria(ocupiedrows, ocupiedcolumns)
        
def condicoesvitoria():
    print("")
Computador()