import random as rd

jogar_novamente = ''

while (jogar_novamente != 'n'):

	chances = 0
	tentativas = 0

	print()
	print("*** Você está no jogo da advinhação ***\n")
	print("Tentes advinhar o número que eu escolhi aleatoriamente! \n")




	nivel = int(input("""Mas antes tens de escolher o nível que deseja jogar! \n
				1 - para fácil \n
				2 - para intermédiario \n
				3 - para difícil """))

	if nivel == 1:
		chances = 20

	elif nivel == 2:
		chances = 12

	elif nivel == 3:
		chances = 5

	minimo = int(input("Qual o número de início do intervalo? "))
	maximo = int(input("Qual o número final do intervalo? "))

	numero_secreto = rd.randrange(minimo, maximo, 1)


	while (chances > tentativas):

		chute = int(input("Digite o número que achas que eu escolhi entre {} e {}: ".format(minimo, maximo)))
		
		
		if chute == numero_secreto:
			print("Parabéns! Você acertou o número que eu escolhi! ", numero_secreto)
			break

		else:
			print("Você errou! Mais sorte na próxima!")
			tentativas += 1




	jogar_novamente = input("Deseja jogar novamente (s/n)? ")

	if jogar_novamente == 'n':
		break
