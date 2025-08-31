print(input('Bem-vinda a Universos! O que lhe posso ajudar? '))

opcao = int(input(
    'Ótimo! Temos muitas opções! Aqui está o Cardápio. Escolha um:\n1: Macchiato \n2: IcedMorango \n3: Mocchatino\n'))


def Macchiato():
    print('Ótimo, fica em R%14.00! Já te trago o seu Macchiato. Aguarde um pouquinho :)')


def IcedMorango():
    print('Esse é maravilhoso! O Iced de Morango é extremamente leve e saboroso. Ótima pedida! Fica em R$18.00')


def Mocchatino():
    print('Ótimo, fica em R%12.00! Já volto com o seu pedido :)')


opcoes = {
    1: Macchiato,
    2: IcedMorango,
    3: Mocchatino
}

opcoes.get(opcao, lambda: print("Opção inválida"))()
metodo = input('Agora qual será a forma de pagamento? ')
Deseja = int(input('Te atribuí um desconto! Mas você escolhe :)| Digite o desconto esperado até 25%: '))
desconto = opcao * Deseja / 100
print('O valor de {} ficou {} com o desconto :)'.format(Deseja, desconto))
