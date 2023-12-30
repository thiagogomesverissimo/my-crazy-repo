x = float(input('Enter a number to find the cube root: '))

epsilon = 0.01
tries = 0

if x < 0:
    low = min(-1.0,x)
    high = 0
else:
    low = 0.0
    high = max(1.0,x)


root = (high + low)/2

while abs(root**3 - x) >= epsilon:
    print('low= ',low, ', high=',high, ', root=',root)
    tries += 1
    if x > root**3:
        low = root
    else:
        high = root
    root = (high + low)/2

print('tries: ', tries)
print(root, 'is a close approximation of cube root of ',x)
