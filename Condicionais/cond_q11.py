def termometro(t):

	if t > 36.5:
		return "Está com febre"
    else:
		return "Sem febre"

t = float(input("Digite um valor real correspondente à temperatura corporal de uma pessoa: "))
print(termometro(t))