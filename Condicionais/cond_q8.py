def oito(x):

    if x == 0:
		return "igual a zero"
	elif x < 0:
		return "negativo"
	elif x > 0:
		return "positivo"

x = int(input("Digite um valor inteiro: "))
print("O número %d é %s." % (x, oito(x)))