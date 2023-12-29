# read an integer and print two integers: root**pwr, 0<pwr<6, otherwise, a message.

num = int(input('Type a integer: '))

root=1
pwr = 0

while root < num:
    i=1
    while i < 6:
        if root**i == num:
            pwr = i
            break
        i += 1
    if pwr != 0:
        break
    root += 1
    

if pwr != 0:
    print("The number %d is equal to %d**%d" % (num,root,pwr))
else:
    print("We didn't find a power between 1 and 5 for %d" % (num))
