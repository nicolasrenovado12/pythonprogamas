def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5))

# Em ordem cr
def a(n):
    b = []
    
    for i in range(0, n):
        b.insert(n, i)
        
    return b

print(a(3))
