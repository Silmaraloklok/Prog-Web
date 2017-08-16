def velocidade(m):
    return m * 3.6


m = float(input("Digite o valor correspondente à medida em m/s: "))
print("%f m/s correspondem a %f km/h." % (m,velocidade(m)))
