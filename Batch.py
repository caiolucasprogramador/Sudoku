from leitor import ler_dicas, tratar_entrada
from validadores import validacao_linha, validacao_coluna,validacao_bloco,tabuleiro_valido
from tabuleiro import criar_tabuleiro, printar_tabuleiro


# Encontra a próxima posição vazia
def espacos_vazios(tab):
    for i in range(9):
        for j in range(9):
            if tab[i][j] == 0:
                return (i, j)
    return None


# Verifica se o número pode ser inserido naquela posição
def valido(tab, valor, pos):
    lin, col = pos
    for j in range(9):
        if tab[lin][j] == valor and j != col:
            return False
    for i in range(9):
        if tab[i][col] == valor and i != lin:
            return False
    bloco_x = col // 3
    bloco_y = lin // 3
    for i in range(bloco_y * 3, bloco_y * 3 + 3):
        for j in range(bloco_x * 3, bloco_x * 3 + 3):
            if tab[i][j] == valor and (i, j) != pos:
                return False

    return True
# Backtraking para resolver o Sudoku
def solucionador_completo(tab):
    pos = espacos_vazios(tab)
    if not pos:
        return True  # Sudoku resolvido

    lin, col = pos
    for num in range(1, 10):
        if valido(tab, num, (lin, col)):
            tab[lin][col] = num

            if solucionador_completo(tab):
                return True

            tab[lin][col] = 0  # backtrack

    return False
# Verifica erros de bluco
def blocos_com_erro(tabuleiro):
    for i in range(9):
        for j in range(9):
            if validacao_bloco(tabuleiro, i, j):
                return True
    return False
# Monta o tabuleiro como a lista de jogadass
def montar_tabuleiro(lista_jogadas):
    tab = [[0 for _ in range(9)] for _ in range(9)]
    for lin, col, val in lista_jogadas:
        tab[lin][col] = val
    return tab

nome_arquivo = input('Digite o caminho do arquivo de dicas: ')
dicas = ler_dicas(nome_arquivo)
jogadast = []

# ele vai processar a dicas
for linha in dicas:
    tratada = tratar_entrada(linha)
    if tratada:
        jogadast.append(tratada)

tabuleiro = montar_tabuleiro(jogadast)
tab_dicas = [linha[:] for linha in tabuleiro]

# validação inicial
if not validacao_linha(jogadast) or not validacao_coluna(jogadast) or blocos_com_erro(tabuleiro):
    printar_tabuleiro(tabuleiro, tab_dicas)
    print('Configuração de dicas inválida')
    exit()

printar_tabuleiro(tabuleiro, tab_dicas)
print('Tabuleiro apenas com as dicas, digite [1] para iniciar o modo batch: ')
resposta = int(input())

if resposta == 1:
    arquivo_batch = input('Digite o caminho do arquivo com as jogadas (Modo Batch): ')
    linhas_batch = ler_dicas(arquivo_batch)

    # solucionador o tabuleiro original (sem jogadas) como referência
    tabuleiro_resolvido = [linha[:] for linha in tabuleiro]
    if not solucionador_completo(tabuleiro_resolvido):
        print("Não foi possível resolver o tabuleiro com as dicas fornecidas.")
        exit()

    print("\nIniciando análise das jogadas do batch...\n")
    for linha in linhas_batch:
        jogada = tratar_entrada(linha)
        if jogada is None:
            continue

        lin, col, val = jogada
        colunas = {1:'A', 2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I'}
        if tab_dicas[lin][col] != 0:
            print(f"Jogada ignorada na linha {lin + 1}, coluna {colunas[col+1]}: posição já preenchida pelas dicas.")
            continue

        valor_correto = tabuleiro_resolvido[lin][col]
        if val != valor_correto:
            print(f"Jogada ERRADA na linha {lin + 1}, coluna {colunas[col+1]}: esperava {valor_correto}, recebeu {val}.")
            continue

        tabuleiro[lin][col] = val
        jogadast.append((lin, col, val))
        print(f"Jogada correta inserida em ({lin + 1}, {colunas[col+1]}): {val}")

    print("\nTabuleiro após aplicação das jogadas válidas:")
    printar_tabuleiro(tabuleiro, tab_dicas)
