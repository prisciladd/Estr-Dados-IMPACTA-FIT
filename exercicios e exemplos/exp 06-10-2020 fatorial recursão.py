def fatorial (n):
    if n == 0: #caso trivial
        return 1
    else:
        return n * fatorial(n-1)

# Programa Principal

print(fatorial(1))
