x = int(input('Enter a integer and I will give you the divisors up to: '))

divisors = ()
for i in range(1,x):
    if x % i == 0:
        divisors = divisors + (i,)

print(divisors)