x = float(input('Enter a number to find a square root: '))

epsilon = 0.01
tries = 0

low = 0.0
high = max(1.0,x) # para incluir raizes de números menores que 1, exemplo, raiz de .25 é 0.5
root = (high + low)/2

while abs(root**2 - x) >= epsilon:
    print('low= ',low, ', high=',high, ', root=',root)
    tries += 1
    if x > root**2:
        low = root
    else:
        high = root
    root = (high + low)/2

print('tries: ', tries)
print(root, 'is a close approximation of square root of ',x)
