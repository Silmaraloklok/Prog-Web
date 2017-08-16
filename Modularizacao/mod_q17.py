def desc(pr, p):

    return pr - (pr * (p / 100))

pr, p = float(input("Digite, respectivamente, o valor correspondente ao preço do produto e o valor correspondente ao percentual de desconto: ")), float(input())
print("O preço do produto é %f." % (desc(pr, p)))