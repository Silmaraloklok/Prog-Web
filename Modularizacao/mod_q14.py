def numInt(n):

    num = str(n)
    if len(num) == 3:
        x = n // 100
        y = (n - (x * 100)) // 10
        return y
    else:
        return 71

n = int(input("Digite um número inteiro com três algarismos: "))
if numInt(n) == 71:
    print("Você não forneceu um número com três algarismos.")
else:
    print("O algarismo das dezenas é %d." % (numInt(n)))