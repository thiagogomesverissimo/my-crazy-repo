def hanoi(discos, pino_from, pino_to, pino_spare):
    if discos == 1:
        print("Mover disco que está no pino " + pino_from + " para pino " + pino_to)
    else:
        hanoi(discos-1,pino_from, pino_spare, pino_to)
        hanoi(1,pino_from, pino_to, pino_spare)
        hanoi(discos-1,pino_spare, pino_to, pino_from)

print("1 Disco:")
hanoi(1,'A','B','C')
print("\n")

print("2 Discos:")
hanoi(2,'A','B','C')
print("\n")

print("3 Discos:")
hanoi(3,'A','B','C')
print("\n")

