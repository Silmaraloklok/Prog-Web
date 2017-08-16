custo = float(input("Digite o valor de custo: "))
percent = float(input("Digite o valor pencentual: "))

percent = (percent/100) * custo
venda = custo + percent
print("O valor de venda é: ",venda)