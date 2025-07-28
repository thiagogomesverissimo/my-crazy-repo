def exp(base,n):
    # base case
    if n == 0:
        return 1
    # inductive step
    return(base * exp(base, n-1))

print(exp(2,4))
print(exp(3,2))
