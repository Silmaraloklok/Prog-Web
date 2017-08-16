def Veloc(k):
    return k / 3.6

k = float(input("Digite o valor correspondente à medida em km/h: "))

print("%f km/h correspondem a %f m/s." % (k, Veloc(k)))