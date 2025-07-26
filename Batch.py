from leitor import ler_dicas, tratar_entrada
from validadores import validacao_linha, validacao_coluna,validacao_bloco
from tabuleiro import printar_tabuleiro

nome_arquivo = input('Digite o caminho do arquivo de dicas: ')


dicas = ler_dicas(nome_arquivo)
jogadast = []



#tratamento geral das dicas, e depois print do tabuleiro(apenas com as dicas, sem as jogadas do batch ainda)
for e in dicas:
    if tratar_entrada(e) is not None:
        jogadast.append(tratar_entrada(e))#loop para preencher a lista com as linhas tratadas e transformadas em tuplas

tabuleiro = [[0 for _ in range(9)] for _ in range(9)] #inicializa o tabuleiro (matriz 9x9)
for lin, col, val in jogadast:#loop para preencher o tabuleiro
    tabuleiro[lin][col] = val
tab_dicas = [linha[:] for linha in tabuleiro] #cópia do tabuleiro original preenchido apenas com as dicas


def blocos_com_erro(tabuleiro):
    for i in range(9):
        for j in range(9):
            if validacao_bloco(tabuleiro, i, j):
                return True
    return False


if not validacao_linha(jogadast) or not validacao_coluna(jogadast) or blocos_com_erro(tabuleiro):
    printar_tabuleiro(tabuleiro,tab_dicas)
    print('As dicas violam as regras do Sudoku.')
    exit()

printar_tabuleiro(tabuleiro,tab_dicas)
print('Tabuleiro apenas com as dicas, digite [1] para iniciar o modo batch: ')
resposta = int(input())
if resposta == 1:
    arquivo_batch = input('Digite o caminho do arquivo com as jogadas (Modo Batch): ')
    jogadas = ler_dicas(arquivo_batch)
    for e in jogadas:
        if tratar_entrada(e) is not None:
            jogadast.append(
                tratar_entrada(e))  # loop para preencher a lista com as linhas tratadas e transformadas em tuplas

    tabuleiro = [[0 for _ in range(9)] for _ in range(9)]  # inicializa o tabuleiro (matriz 9x9)
    for lin, col, val in jogadast:  # loop para preencher o tabuleiro
        tabuleiro[lin][col] = val
    tab_dicas = [linha[:] for linha in tabuleiro]  # cópia do tabuleiro original preenchido apenas com as dicas


    def blocos_com_erro(tabuleiro):
        for i in range(9):
            for j in range(9):
                if validacao_bloco(tabuleiro, i, j):
                    return True
        return False


    if not validacao_linha(jogadast) or not validacao_coluna(jogadast) or blocos_com_erro(tabuleiro):
        printar_tabuleiro(tabuleiro, tab_dicas)
        print('O MODO BATCH IDENTIFICOU JOGADAS QUE VIOLAM REGRAS DO SUDOKU!!!')
        exit()
print('Seu tabuleiro após verificações do Batch:')
printar_tabuleiro(tabuleiro,tab_dicas)
