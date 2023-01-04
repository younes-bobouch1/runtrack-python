def nombres():
    for nombres in range(0, 101):
        if nombres in [26, 37, 88]:
            continue
        print(nombres)


nombres()