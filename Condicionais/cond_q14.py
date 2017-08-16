def quatorze(ano):

	if 2020 - ano >= 16:
		return "Tu poderás votar"
	else:
		return "Tu não poderás votar"

a = int(input("Digite o valor correspondente ao teu ano de nascimento: "))
print(quatorze(a))