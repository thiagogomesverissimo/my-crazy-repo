# find a cube root by exhaustive attemps using for

x = int(input('Enter a integer: '))

for i in range(0,abs(x)+1):
    if i**3 >= abs(x):
        break

if i**3 != abs(x):
    print("%d is not a cube perfect" % (x))
else:
    if x < 0:
        i = -i
    print('The cube root of %d is %d' % (x,i))
