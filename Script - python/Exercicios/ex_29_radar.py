vel = float(input('Digite a velocidade do carro: '))
if(vel > 80):
    print('MULTADO! Você excedeu o limite permitido de 80km/h')
    multa = (vel - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')