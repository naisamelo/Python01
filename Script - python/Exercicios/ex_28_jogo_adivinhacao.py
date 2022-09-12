from random import randint
computador = randint(0, 5) #Faz o computador "Pensar"

print('-=-' * 20)
print('vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

jogador = int(input("Em que número eu pensei? ")) #Jogador tenta adivinhar

if computador == jogador:
    print("Parabéns, você consegiu me vencer!")
else:
    print("GANHEI! Eu pensei no número {} e não no número {}".format(computador, jogador))