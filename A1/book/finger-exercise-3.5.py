k = float(input('Enter a value for me to find a square root: '))

# f(x) = x**2 - k
# f'(x) = 2x (derivada de f(x))
# novo guess: guess - (f(guess)/f'(guess))

episilon = 0.01
tries = 0

guess = k/2.0

while abs(guess*guess - k) >= episilon:
    tries += 1
    guess = guess - (guess**2 - k)/(2*guess)

print('tries: ', tries)
print('Square root of ', k, ' is about ', guess)
