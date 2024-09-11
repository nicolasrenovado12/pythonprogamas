def is_a_triangle(lado1, lado2, base):  
    if lado1 + lado2 <= base:
        return False
    else:
        return True

print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))
