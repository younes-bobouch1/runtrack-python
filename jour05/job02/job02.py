def dessin(h, l):
    c = '|' + '-' * (h - 1) + '|\n';

    print(c + c.replace(*'- ') * (l - 1) + c)


dessin(10, 3)

"Devoir non compris, ce n'est pas mon devoir"