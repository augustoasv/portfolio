"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um número inteiro: ')

if numero.isdigit():
    inteiro = int(numero)
    resto = int(numero) % 2
    if resto != 0:
        print(f'{numero} é ímpar')

    else:
        print(f'{numero} é par')
else:
    print('Este número não é inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Digite a hora: ')
hora = int(hora.replace(':', ''))

if hora >= 0000 and hora <= 1159:
    print('Bom dia')

elif hora >= 1200 and hora <= 1759:
    print('Boa tarde')

elif hora >= 1800 and hora <= 2359:
    print('Boa noite')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu primeiro nome: ')
quantidade = len(nome)

if quantidade <= 4:
    print('Seu nome é pequeno')
elif 5 <= quantidade <= 6:
    print('Seu nome é normal')
elif quantidade > 6:
    print('Seu nome é muito grande')