def quad(l):

	return l * l, l * 4

l = float(input("Digite o valor correspondente à medida do lado do quadrado: "))
a, p = quad(l)
print("A área desse quadrado é %f. O perímetro, %f." % (a, p))