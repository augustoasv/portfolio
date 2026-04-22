import os

lista_compras = []

while True:
    opcoes = input('Escolha uma opção:\n[i]nserir, [a]pagar, [l]istar, [s]air: ').strip().lower()

# Comando de sair
    if opcoes.startswith('s'):
        break

# Comando de inserir item
    if opcoes.startswith('i'):
        os.system('cls')
        valor = input('Valor para inserir: ').strip()
        if valor:
            lista_compras.append(valor)
        else:
            print('Você não pode inserir um item vazio!')

# Comando de apagar item da lista
    elif opcoes.startswith('a'):
        os.system('cls')
        if not lista_compras:
            print('A lista está vazia, nada para apagar.')
            continue

        print('--- SUA LISTA ---')
        for i, valor in enumerate(lista_compras):
            print(f'{i}: {valor}')    # Coloquei para aparacer a lista para facilitar
            
        apagar_indice = input('Qual índice você quer apagar?: ')

# Treinando a utilização do Try/Except com os erros que apareceram nos testes
        try:
            indice = int(apagar_indice)
            print(f'Item "{indice}" removido com sucesso!')
            del lista_compras[indice]
        except ValueError:
            print('Erro: Digite apenas números inteiros.')
        except IndexError:
            print('Erro: Esse índice não existe na lista.')

# Comando de listar
    elif opcoes.startswith('l'):
        os.system('cls')
        if not lista_compras:
            print('Nada para listar.')
        else:
            print('--- SUA LISTA ---')
            for i, valor in enumerate(lista_compras):
                print(f'{i}: {valor}')
    
    else:
        print('Opção inválida. Escolha entre i, a, l ou s.')
