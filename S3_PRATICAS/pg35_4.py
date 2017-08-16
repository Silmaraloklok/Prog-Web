nome = input("Digite seu nome:")
end = input("Digite seu endereço:")
try:
    tel = int(input("Digite seu telefone:"))
    print("Os dados informados(nome, endereço e telefone) foram respectivamente: ", nome,", ", end,", ",tel)
except:
    print("Digite apenas números no espaço telefone!")
