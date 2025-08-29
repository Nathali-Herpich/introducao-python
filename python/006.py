import random

print('Bem-Vindo(a) ao jogo da adivinhação')
print('Você terá três tentativas para adivinhar o número')
print('Está preparado(a)?')
numero_secreto = random.randint(1, 100)
tentativas = 3
acertou = False

print('Adivinhe o número (entre 1 a 100):')

while not acertou:
    tentativas = int(input('Digite seu palpite: '))
    tentativas += 3

if tentativas == numero_secreto:
    print('Parábens! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas')
    acertou = True
elif tentativas < numero_secreto:
    print('O número é maior')
else:
    print('O número é menor')
