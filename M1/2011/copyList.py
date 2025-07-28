def copyList(L_source,L2_dest):
    for i in L_source:
        L2_dest.append(i)

L1 = [1,2,3]
L2 = []

copyList(L1,L2)

L1[2] = 666

print('L1', L1)
print('L2', L2)

