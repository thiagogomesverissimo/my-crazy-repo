# give a string like: s='1.23,2.4,3.123', sum the numbers in s

s = input('Type a string like 1.23,2.4,3.123: ')
total = 0
for i in s:
    if i != '.' and i !=',':
        total += int(i)

print('The sum of numbers id %d' % (total))