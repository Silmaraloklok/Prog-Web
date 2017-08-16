def mp(x, y, w, z):

    return (x + (y * 2) + (w * 3) + (z * 4)) / 10

a, b, c, d = float(input("Digite quatro números reais: ")), float(input()), float(input()), float(input())
print("A média ponderada dos números é %f." % (mp(a, b, c, d)))