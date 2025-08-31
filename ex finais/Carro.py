valor = int(input('Digite a quantidade de Km percorridos do carro alugado: '))
dias = int(input('Digite a quantidade de dias alugado '))
diasAlugado = (valor * 0.15) + (dias * 60)
print('Foram ', valor, ' Km percorridos e', dias, ' dias alugados, então fica {} reais a se pagar'.format(diasAlugado))
