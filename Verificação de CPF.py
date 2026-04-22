import re
import sys

cpf = input('Digite um CPF: ')
cpf_limpo = re.sub(r'[^0-9]', '', cpf)
nove_dig = cpf_limpo[:9]
contador_regressivo_1 = 10
soma_1 = 0

tudo_igual = cpf_limpo[0] * len(cpf_limpo)

if cpf_limpo == tudo_igual:
    print('Entrada não permitida')
    sys.exit()

# Primeiro digito
for digitos in nove_dig:
    soma_1 += int(digitos) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = (soma_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

print(f'O primeiro digito do CPF é: {digito_1}')

# Segundo digito
dez_digitos = nove_dig + str(digito_1)
contador_regressivo_2 = 11
soma_2 = 0

for digitos in dez_digitos:
    soma_2 += int(digitos) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_2 = (soma_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

print(f'O segundo digito do CPF é: {digito_2}')

# Checando se o CPF é válido
cpf_novo = dez_digitos + str(digito_2)

if cpf_novo == cpf_limpo:
    print('Este CPF é válido')
else:
    print('Este CPF é inválido')