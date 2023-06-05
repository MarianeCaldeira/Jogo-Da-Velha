from random import randint
from time import sleep

veia = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

# Função que altera os valores conforme o valor digitado, ou o valor sorteado pelo computador!
def posicao(p, l):
    x = 0
    while x == 0:
        for i in range(3):
            l1 = 7
            l2 = 4
            l3 = 1
            for k in range(3):
                if i == 0:
                    if p == l1 and veia[i][k] == ' ':
                        veia[i][k] = l
                        x = 1
                        break
                elif i == 1:
                    if p == l2 and veia[i][k] == ' ':
                        veia[i][k] = l
                        x = 1
                        break
                elif i == 2:
                    if p == l3 and veia[i][k] == ' ':
                        veia[i][k] = l
                        x = 1
                        break
                l1 += 1
                l2 += 1
                l3 += 1
        if i == 2 and x == 0:
            if jogo == 2 or player % 2 != 0:
                print('\033[0;31mPosição Ocupada! Tente em outra posição.\033[m')
                p = int(input('Digite a posição: '))
            else:
                p = randint(1, 9)


print('\n                  \033[0;33mJOGO DA VELHA\033[m              ')
print('                    7 | 8 | 9 ')
print('                   ---+---+---')
print('                    4 | 5 | 6 ')
print('                   ---+---+---')
print('                    1 | 2 | 3 ')
print('                   ---+---+---')
print('\033[0;31m↑ Para jogar digite a posição de acordo com o exemplo a cima ↑\033[m\n')
print('\033[0;33mDigite(1):\033[m para jogar contra a máquina\n' 
      '\033[0;33mDigite(2):\033[m para jogar contra outro jogador')
msg = '\033[0;33mInforme a opção desejada: \033[m'
while (jogo := int(input(msg))) not in (1, 2):
    print('\033[0;31mOpção Inválida!\033[m')

# sorteio para saber qual jogador irá iniciar o jogo.
turno = 0
player = randint(0, 1)
while True:
    turno += 1
    if player % 2 != 0:
        print('\n\033[0;32mJogador 1\033[m, sua vez!')
        pos = int(input('\033[0;32mJogador 1\033[m, faça sua jogada: '))
        let = '\033[0;32mX\033[m'
        posicao(pos, let)
        player += 1

        print(f' {veia[0][0]} | {veia[0][1]} | {veia[0][2]} ')
        print('---+---+---')
        print(f' {veia[1][0]} | {veia[1][1]} | {veia[1][2]} ')
        print('---+---+---')
        print(f' {veia[2][0]} | {veia[2][1]} | {veia[2][2]} ')
        print('---+---+---\n')

    else:
        if jogo == 1:
            print('\033[0;33mDeixe-me pensar na minha jogada...\033[m')
            sleep(1.5)
        else:
            print('\033[0;34mJogador 2\033[m, sua vez!')

        if jogo == 1:
            pos = randint(1, 9)
            let = '\033[0;34mO\033[m'
            posicao(pos, let)
            player += 1
        else:
            pos = int(input('\033[0;34mJogador 2\033[m, faça sua jogada: '))
            let = '\033[0;34mO\033[m'
            posicao(pos, let)
            player += 1

        print(f' {veia[0][0]} | {veia[0][1]} | {veia[0][2]} ')
        print('---+---+---')
        print(f' {veia[1][0]} | {veia[1][1]} | {veia[1][2]} ')
        print('---+---+---')
        print(f' {veia[2][0]} | {veia[2][1]} | {veia[2][2]} ')
        print('---+---+---')

    # calcular se houve um vencedor ou se o jogo deu empate
    fim = False
    win = 0
    for x in range(3):
        if veia[x][0] != ' ' and veia[x][0] == veia[x][1] == veia[x][2]:
            win = 1
    for x in range(3):
        if veia[0][x] != ' ' and veia[0][x] == veia[1][x] == veia[2][x]:
            win = 1
    if veia[0][2] != ' ' and ((veia[0][2] == veia[1][1] == veia[2][0]) or (veia[0][0] == veia[1][1] == veia[2][2])):
        win = 1
    if win == 1:
        break
    if turno == 9:
        fim = True
        print('\033[0;31mFim de Jogo! Deu Velha!\033[m')
        break
if not fim:
    if player % 2 == 0:
        print('Fim de Jogo. \033[0;32mJogador 1 ganhou!\033[m')
    elif jogo == 2:
        print('Fim de Jogo. \033[0;34mJogador 2 ganhou!\033[m')
    else:
        print('\033[0;33mFim de jogo. Eu ganhei!\033[m')