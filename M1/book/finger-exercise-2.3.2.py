# Asks the user to input 10 integers, and then prints the largest odd number that was entered.

odd = 0
i=1
while i<11:
    x = int(input('Enter the %dst integer number: ' % (i)))
    if (x%2 != 0) and (x > odd):
        odd = x
    i += 1

if x != 0:
    print('The largest odd number entered was %d' % (odd))
else:
    print('No odd number was provided!')