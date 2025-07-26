from leitor import ler_dicas, tratar_entrada
from validadores import validacao_linha, validacao_coluna, validacao_bloco
from tabuleiro import printar_tabuleiro
from solucionador import solucionador_completo

# Verifica erros de bloco
def blocos_com_erro(tabuleiro):
    for i in range(9):
        for j in range(9):
            if validacao_bloco(tabuleiro, i, j):
                return True
    return False

# Monta o tabuleiro com base nas jogadas
def montar_tabuleiro(lista_jogadas):
    tab = [[0 for _ in range(9)] for _ in range(9)]
    for lin, col, val in lista_jogadas:
        tab[lin][col] = val
    return tab

# Lê as dicas, analisa as jogadas e resolve o tabuleiro
def modo_batch():
    nome_arquivo = input('Digite o caminho do arquivo de dicas: ')
    dicas = ler_dicas(nome_arquivo)
    jogadast = []

    # Processa as dicas
    for linha in dicas:
        tratada = tratar_entrada(linha)
        if tratada:
            jogadast.append(tratada)

    tabuleiro = montar_tabuleiro(jogadast)
    tab_dicas = [linha[:] for linha in tabuleiro]  # cópia do tabuleiro com apenas as dicas

    # Validação inicial do tabuleiro
    if not validacao_linha(jogadast) or not validacao_coluna(jogadast) or blocos_com_erro(tabuleiro):
        printar_tabuleiro(tabuleiro, tab_dicas)
        print('Configuração de dicas inválida')
        return

    printar_tabuleiro(tabuleiro, tab_dicas)

    arquivo_batch = input('Digite o caminho do arquivo com as jogadas (Modo Batch): ')
    linhas_batch = ler_dicas(arquivo_batch)

    # Resolve o tabuleiro original com as dicas como referência
    tabuleiro_resolvido = [linha[:] for linha in tabuleiro]
    if not solucionador_completo(tabuleiro_resolvido):
        print("Não foi possível resolver o tabuleiro com as dicas fornecidas.")
        return

    print("\nIniciando análise das jogadas do batch...\n")
    colunas = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I'}

    for linha in linhas_batch:
        jogada = tratar_entrada(linha)
        if jogada is None:
            continue

        lin, col, val = jogada

        if tab_dicas[lin][col] != 0:
            print(f"Jogada ignorada na linha {lin + 1}, coluna {colunas[col + 1]}: posição já preenchida pelas dicas.")
            continue

        valor_correto = tabuleiro_resolvido[lin][col]
        if val != valor_correto:
            print(f"Jogada ERRADA na linha {lin + 1}, coluna {colunas[col + 1]}: esperava {valor_correto}, recebeu {val}.")
            continue

        tabuleiro[lin][col] = val
        jogadast.append((lin, col, val))
        print(f"Jogada correta inserida em ({lin + 1}, {colunas[col + 1]}): {val}")

    print("\nTabuleiro após aplicação das jogadas válidas:")
    printar_tabuleiro(tabuleiro, tab_dicas)