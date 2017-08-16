def Valor(a):
    return (a*70/100)

x = int(input("Digite um valor em reais(R$): "))
x= Valor(x)
print("70% do valor digitado é: ",x)