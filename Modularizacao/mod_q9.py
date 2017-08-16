def num(x):

	return x - 1, x + 1

x = int(input("Digite um número inteiro: "))
a, s = num(x)
print("O antecessor de %d é %d. O sucessor, %d." % (x, a, s))
