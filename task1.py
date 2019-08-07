S = int(input('S ='))
A = int(input('A ='))
D = A ** 2 + 8 * S
x1 = (-A + D**0.5) // 2
x2 = (-A - D**0.5) // 2
x = x1 if x1>0 else x2
h = round(x + A, 2)
print('h = '+str(h))
