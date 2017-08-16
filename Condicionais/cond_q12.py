def multip(x):

	if x % 7 == 0:
		return "O número é múltiplo de 7"
    else:
		return "O número não é múltiplo de 7"

x = int(input("Digite um valor inteiro: "))
print(multip(x))