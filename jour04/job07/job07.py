L = [8, 24, 48, 2, 16]

nbr = 0

for i in range(len(L)):
    if L[i] % 3 == 0:
        nbr = nbr + 1

print(nbr)