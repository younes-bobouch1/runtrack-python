def fonc(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")

    if type == "fruits" and saison == "ete":
        print("Poire, fraise, cassis")

    if type == "legume" and saison == "hiver":
        print("carotte, topinambour, endive")

    if type == "legume" and saison == "ete":
        print("artichaut, aubergine,navet")


fonc("fruits", "hiver")
fonc("fruits", "ete")
fonc("legume", "hiver")
fonc("legume", "ete")