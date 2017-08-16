user = input("Digite um nome de usuário e a sua respectiva senha (não podem ser iguais):\nUsername: ")
passw = input("Password: ")

while user == passw:

	user = input("Erro: os valores não podem ser iguais.\nUsername: ")
	passw= input("Password: ")