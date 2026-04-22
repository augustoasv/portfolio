while True:
    num1 = input('Digite o primeiro número: ')  # Primeiro número para cálculo
    num2 = input('Digite o segundo número: ')  # Segundo número para cálculo
    operador = input('Escolha, +, -, * ou /: ')  # Escolha da operação no cálculo
    operadores_permitidos = '+-*/'  # Operadores permitidos
    num1_float = 0
    num2_float = 0

# Checando se tem apenas um operador digitado
    if len(operador) > 1:
        print('Digite apenas 1 operador.')
        continue

# Checando se o operador digitado é válido
    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

# Laço da calculadora
    try:
        num1_float = float(num1)
        num2_float = float(num2)

        if operador == '+':  # Operador de soma
            print(f'Resultado: {num1_float + num2_float}')
        elif operador == '-':  # Operador de subtração
            print(f'Resultado: {num1_float - num2_float}')
        elif operador == '*':  # Operador de multiplicação
            print(f'Resultado: {num1_float * num2_float}')
        elif operador == '/':  # Operador de divisão
            if num2_float == 0:  # Limitando que divisão por zero não é permitida
                print('Erro: Divisão por zero não é permitida.')
            else:
                print(f'Resultado: {num1_float / num2_float}')

# Erro que aparece se for digitado algo diferente pelo usuário
    except:
        print('Erro: Você não digitou números válidos (use "." para decimais).')
        continue

# No fim do cálculo, pergunta se o usuário quer sair da calculadora
    sair = input('Você quer sair? [s]air: ').lower().startswith('s')
    if sair:
        break