#funcoes validadoras para montar o tabuleiro com as dicas iniciais
def validacao_linha(dicastratadas):
    nova_lista = [(tupla[0], tupla[2]) for tupla in dicastratadas]
    if len(nova_lista) != len(set(nova_lista)):
        return False
    return True


def validacao_coluna(dicastratadas):
    lista_nova = [(tupla[1], tupla[2]) for tupla in dicastratadas]
    if len(lista_nova) != len(set(lista_nova)):
        return False
    return True


def validacao_bloco(tabuleiro, lin, col):
    linha_base = 0
    coluna_base = 0
    bloco = []
    if lin <= 2:
        linha_base = 0
    elif lin <= 5:
        linha_base = 3
    else:
        linha_base = 6

    if col <= 2:
        coluna_base = 0
    elif col <= 5:
        coluna_base = 3
    else:
        coluna_base = 6
    for i in range(linha_base, linha_base + 3):
        for j in range(coluna_base, coluna_base + 3):
            if tabuleiro[i][j] != 0 and tabuleiro[i][j] in bloco:
                return True #tem repetido
            bloco.append(tabuleiro[i][j])
    return False #nao tem repetido

#funçao que verifica se o tabuleiro esta completo
def tabuleiro_completo(tabuleiro): #funçao que verifica se o tabuleiro esta completo
    for i in tabuleiro:
        if 0 in i:
            return False
    return True


def tabuleiro_valido(tabuleiro, dicas):
    if not validacao_linha(dicas) or not validacao_coluna(dicas):
        return False

    for i in range(9):
        for j in range(9):
            if validacao_bloco(tabuleiro, i, j):
                return False  # tem repetição
    return True

#validacao linha e coluna do modo interativo

def validacao_linhai(tabuleiro, lin, col):
    valor = tabuleiro[lin][col]
    for j in range(9):
        if j != col and tabuleiro[lin][j] == valor:
            return False
    return True


def validacao_colunai(tabuleiro, lin, col):
    valor = tabuleiro[lin][col]
    for i in range(9):
        if i != lin and tabuleiro[i][col] == valor:
            return False
    return True

def validacao_blocoi(tabuleiro,lin,col):
    linha_base = (lin // 3) * 3
    coluna_base = (col // 3) * 3
    valor = tabuleiro[lin][col]
    
    for i in range(linha_base, linha_base + 3):
        for j in range(coluna_base, coluna_base + 3):
            if (i, j) != (lin, col) and tabuleiro[i][j] == valor:
                return False  
    return True 