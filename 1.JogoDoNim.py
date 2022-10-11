def computador_escolhe_jogada(n,m):
    a = 0
    if n == m:
        return m
    if n < m:
        return n
    if n > m:
        for i in range(1,m+1):
            if (n - i) % (m+1) == 0:
                a = i
        if a == 0:
            return m
        return a


def usuario_escolhe_jogada(n,m):
    usuario_retira = int(input('Quantas peças você vai tirar? '))
    while usuario_retira > m or usuario_retira > n or usuario_retira <= 0:
        print("Oops! Jogada inválida! Tente de novo.")
        usuario_retira = int(input('Quantas peças você vai tirar? '))
    return usuario_retira


def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    pecas_restantes = n
    pecas_retiradas = 0
    next_player = ''
    if n % (m+1) == 0:
        print('Voce começa!')
        next_player = 'usuario'
    else:
        print('O computador começa!')
        next_player = 'computador'
    while True:
        if next_player == 'usuario':
            pecas_retiradas = usuario_escolhe_jogada(pecas_restantes,m)
            pecas_restantes -= pecas_retiradas
            next_player = 'computador'
            if pecas_restantes > 1:
                print(f'Você tirou {pecas_retiradas} peças.\nAgora restam {pecas_restantes} peças no tabuleiro.')
            elif pecas_restantes == 1:
                print(f'Você tirou {pecas_retiradas} peças.\nAgora resta apenas uma peça no tabuleiro.')
            else:
                print(f'Você tirou {pecas_retiradas} peças.')
                print("Fim do jogo!",end=' ')
                return 'Você ganhou!'
        else:
            pecas_retiradas = computador_escolhe_jogada(pecas_restantes, m)
            pecas_restantes -= pecas_retiradas
            next_player = 'usuario'
            if pecas_restantes > 1:
                print(f'O computador tirou {pecas_retiradas} peças.\nAgora resta apenas {pecas_restantes} peças no tabuleiro.')
            elif pecas_restantes == 1:
                print(f'O computador tirou {pecas_retiradas} peças.\nAgora resta apenas uma peça no tabuleiro.')
            else:
                print(f'O computador tirou {pecas_retiradas} peças.')
                print('Fim do jogo!', end= '')
                return 'O computador ganhou!'


def campeonato():
    user_vence = 0
    pc_vence = 0
    for i in range(3):
        print(f"**** Rodada {i+1} ****")
        a = partida()
        print(a)
        if a == 'Você ganhou!':
            user_vence += 1
        else:
            pc_vence += 1
    print('**** Final do campeonato! ****')
    return f'Placar: Você {user_vence} X {pc_vence} Computador'

jogo = int(input('''Bem-vindo ao jogo do NIM! Escolha:
1 - para jogar uma partida isolada
2 - para jogar um campeonato '''))
if jogo == 1:
    print('Voce escolheu uma partida isolada!')
    print(partida())
elif jogo == 2:
    print('Voce escolheu um campeonato!')
    print(campeonato())