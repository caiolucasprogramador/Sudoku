from leitor import ler_dicas, tratar_entrada
from validadores import (
    validacao_linha, validacao_coluna, validacao_bloco,
    tabuleiro_completo, validacao_colunai, validacao_linhai, validacao_blocoi
)
from tabuleiro import printar_tabuleiro


def blocos_com_erro(tabuleiro):
    for i in range(9):
        for j in range(9):
            if validacao_bloco(tabuleiro, i, j):
                return True
    return False


def tratar_jogada(linha):
    try:
        linha = linha.replace(' ', '')
        linha = linha.replace('=', ':')
        linha = linha.upper()

        if ':' in linha and not linha.split(':')[1].startswith(' '):
            linha = linha.replace(':', ': ')

        if ':' not in linha:
            return None

        parte1, valor = linha.split(':')
        letra, num = parte1.split(',')

        valcol = {'A': 0, 'B': 1, 'C': 2,
                  'D': 3, 'E': 4, 'F': 5,
                  'G': 6, 'H': 7, 'I': 8}

        if letra not in valcol:
            return None

        col = valcol[letra]
        lin = int(num) - 1
        val = int(valor.strip())

        jogadas_validas = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        if col not in jogadas_validas or lin not in jogadas_validas or not (1 <= val <= 9):
            return None

        return lin, col, val
    except:
        return None


def mostrar_possibilidades(tabuleiro, letra, num):
    valcol = {'A': 0, 'B': 1, 'C': 2,
              'D': 3, 'E': 4, 'F': 5,
              'G': 6, 'H': 7, 'I': 8}
    vallin = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    if letra in valcol and int(num) in vallin:
        col = valcol[letra]
        lin = int(num) - 1

        if tabuleiro[lin][col] != 0:
            return 'Essa célula já está preenchida.', None
        else:
            possibilidades = []
            for i in range(1, 10):
                tabuleiro[lin][col] = i
                if validacao_linhai(tabuleiro, lin, col) and validacao_blocoi(tabuleiro, lin, col) and validacao_colunai(tabuleiro, lin, col):
                    possibilidades.append(i)
                tabuleiro[lin][col] = 0
            return None, possibilidades
    else:
        return 'Comando de ajuda mal formatado', None


def apagar_jogada(tabuleiro, tab_dicas, letra, num):
    valcol = {'A': 0, 'B': 1, 'C': 2,
              'D': 3, 'E': 4, 'F': 5,
              'G': 6, 'H': 7, 'I': 8}
    vallin = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    if letra in valcol and int(num) in vallin:
        col = valcol[letra]
        lin = int(num) - 1

        if tabuleiro[lin][col] == 0:
            print('Essa célula já está vazia')
        elif tab_dicas[lin][col] != 0:
            print('Não é possível apagar uma dica')
        else:
            tabuleiro[lin][col] = 0
            print(f'A celula {letra}, {num} foi apagada')
            printar_tabuleiro(tabuleiro, tab_dicas)
    else:
        print('Comando de remoçao mal formatado')


def processar_jogada(tabuleiro, tab_dicas, lin, col, val):
    if tab_dicas[lin][col] != 0:
        print('Essa posiçao contém uma dica e nao pode ser alterada.')
        return False

    if tabuleiro[lin][col] != 0:
        print('Essa posiçao ja esta preenchida')
        sobr = input('Deseja sobrescrever o valor?\nS para sobrescrever\nN para manter como está: \n').strip().upper()
        while sobr not in ('S', 'N'):
            print('Resposta inválida, digite S ou N.')
            sobr = input('Deseja sobrescrever o valor?\nS para sobrescrever\nN para manter como está: \n').strip().upper()

        if sobr == 'S':
            tabuleiro[lin][col] = val
            if not validacao_linhai(tabuleiro, lin, col) or not validacao_colunai(tabuleiro, lin, col) or not validacao_blocoi(tabuleiro, lin, col):
                print('jogada inválida: essa jogada fere as regras do sudoku, jogue novamente: ')
                tabuleiro[lin][col] = 0
                return False

            else:
                printar_tabuleiro(tabuleiro, tab_dicas)
                if tabuleiro_completo(tabuleiro):
                    print('\033[32mSudoku completado!\033[m')
                    return True
        else:
            print('Jogada cancelada')
            return False

    else:
        tabuleiro[lin][col] = val
        if not validacao_linhai(tabuleiro, lin, col) or not validacao_colunai(tabuleiro, lin, col) or not validacao_blocoi(tabuleiro, lin, col):
            print('Jogada inválida: essa jogada fere as regras do sudoku, jogue novamente: ')
            tabuleiro[lin][col] = 0
            return False
        else:
            printar_tabuleiro(tabuleiro, tab_dicas)
            if tabuleiro_completo(tabuleiro):
                print('\033[32mSudoku completado!\033[m')
                return True

    return False


def modo_interativo(dicast):

    if len(dicast) < 1 or len(dicast) > 80:
        print('Número de pistas inválido.')
        return

    tabuleiro = [[0 for _ in range(9)] for _ in range(9)]
    for lin, col, val in dicast:
        tabuleiro[lin][col] = val
    tab_dicas = [linha[:] for linha in tabuleiro]

    if not validacao_linha(dicast) or not validacao_coluna(dicast) or blocos_com_erro(tabuleiro):
        printar_tabuleiro(tabuleiro, tab_dicas)
        print("As dicas violam as regras do Sudoku.")
        return

    jogo_ativo = True

    while jogo_ativo:
        printar_tabuleiro(tabuleiro, tab_dicas)

        print('\nDigite sua jogada no formato COL,LIN: VALOR\n\nCaso queira saber as jogadas disponíveis para determinada posição digite ?COL,LIN\nE para apagar a jogada digite !COL,LIN')
        jogada = input('Jogada: ').strip().upper()

        resultado = tratar_jogada(jogada)

        if resultado is not None:
            lin, col, val = resultado
            if processar_jogada(tabuleiro, tab_dicas, lin, col, val):
                jogo_ativo = False

        elif jogada.startswith('?'):
            try:
                resto = jogada[1:]
                letra, num = resto.split(',')
                printar_tabuleiro(tabuleiro, tab_dicas)  # imprime primeiro o tabuleiro
                print()
                erro_msg, possibilidades = mostrar_possibilidades(tabuleiro, letra, num)
                if erro_msg:
                    print(erro_msg)
                else:
                    print(f'Valores validos para a celula {letra}, {num}: {possibilidades}')  # imprime depois a mensagem
            except Exception:
                print('Comando de ajuda mal formatado')

        elif jogada.startswith('!'):
            try:
                resto = jogada[1:]
                letra, num = resto.split(',')
                apagar_jogada(tabuleiro, tab_dicas, letra, num)
            except Exception:
                print('Comando de remoçao mal formatado')

        else:
            print('Essa jogada é inválida, tente novamente.')