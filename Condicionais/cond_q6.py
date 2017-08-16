def seis(x):

	if x > 20:
		return "Vá ao cinema"
    else:
		return "Fique vendo TV"

x = float(input("Quanto dinheiro você tem (em R$): "))
print(seis(x))