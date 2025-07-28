# find a cube root by exhaustive attemps using while

x = int(input('Enter a integer: '))
i = 0 

while i**3 < abs(x): 
    i += 1

if i**3 != abs(x):
    print("%d is not a cube perfect" % (x))
else:
    if x < 0:
        i = -i
    print('The cube root of %d is %d' % (x,i))
