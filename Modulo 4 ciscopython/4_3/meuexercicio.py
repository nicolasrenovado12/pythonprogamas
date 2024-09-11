def b(tabuada):
    a = []
    
    for i in range(1, 11):
        a.append(tabuada * i)
        
    return a
tabuada = int(input(""))
print(b(tabuada))