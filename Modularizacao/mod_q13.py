def t(x):

    if x >= 2013:
		return 0
    else:
    	return 2013 - x

x = int(input("Digite o ano de nascimento: "))
i = t(x)
if i == 0:
    print("Essa pessoa ainda não nasceu.")
else:
    print("Essa pessoa tem %d anos." % (i))
