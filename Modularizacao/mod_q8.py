def div(x, y):

	q = x // y
	r = x % y
	return q, r

x, y = int(input("Digite os  dois números inteiros: ")), int(input())
q, r = div(x, y)
print("O quociente da divisão de %d por %d é %d com resto, %d." % (x, y, q, r))
