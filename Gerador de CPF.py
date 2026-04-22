import random

nove_dig = ''
for i in range(9):
    nove_dig += str(random.randint(0, 9))

contador_regressivo_1 = 10
soma_1 = 0

# Primeiro digito
for digitos in nove_dig:
    soma_1 += int(digitos) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = (soma_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

# Segundo digito
dez_digitos = nove_dig + str(digito_1)
contador_regressivo_2 = 11
soma_2 = 0

for digitos in dez_digitos:
    soma_2 += int(digitos) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_2 = (soma_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

# Checando se o CPF é válido
cpf_novo = dez_digitos + str(digito_2)

cpf_formatado = f"{cpf_novo[:3]}.{cpf_novo[3:6]}.{cpf_novo[6:9]}-{cpf_novo[9:]}"
print(cpf_formatado)