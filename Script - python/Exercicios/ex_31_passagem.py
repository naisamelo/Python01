distancia = float(input('Qual a distância: '))
if distancia <= 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45
print('Sua passagem vai custar R${:.2f}'.format(passagem))

'''passagem = distancia * 0.50 if distancia <= 200 else distancia * 0.45'''
