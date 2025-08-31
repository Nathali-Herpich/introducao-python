salario = float(input('Digite seu salario: '))
percentual = float(input('Digite a porcentagem que deseja de aumento até 25%: '))
reajuste = salario + (salario * percentual / 100)
print('O seu salário que antes era {}, agora com o reajuste ficou em {} '.format(salario, reajuste))