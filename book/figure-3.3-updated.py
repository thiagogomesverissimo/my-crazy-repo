x = float(input('Enter a number to find a square root: '))

epsilon = 0.01
step = epsilon**2
root = 0
tries = 0

while (abs(root**2 -x) >= epsilon) and root*root<=x:
    root += step
    tries += 1

print('tries: ', tries)
# caso 1: Se saimos do loop por causa da condição root<=x, a condição
# abs(root**2 -x) >= epsilon continua verdadeira, e não encontramos a raiz
if abs(root**2 -x) >= epsilon:
    print('failed to find square root of ', x)

# caso 2: se saímos do while por causa de abs(root**2 -x) >= epsilon,
# achamos uma boa aproximação
else:
    print(root, 'is a close approximation of square root of ',x)
