import os

palavra_secreta = 'arquipelogo'
tentativas = 0
letras_certas = ''

while True:
    letra_digitada = input('Digite apenas uma letra: ').lower()
    tentativas += 1

# Checando se tem mais de um digito na entrada
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra!')
        continue

# Se a palavra secreta, tiver a letra digitada, ele adiciona atraves da concatenação
# na variavel vazia 'letras_certas'
    if letra_digitada in palavra_secreta:
        letras_certas += letra_digitada

# Monta a palavra que será exibida na tela. O laço percorre cada letra da palavra secreta,
# se ela já estiver nas letras acertadas, a letra é revelada, senão, adiciona um '*' no lugar.
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_certas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

# Mensaegem que aparece quando o jogador acerta a palavra
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU! PARABENS!')
        print( 'A palavra era: ', palavra_formada)
        print(f'Você tentou {tentativas}x')