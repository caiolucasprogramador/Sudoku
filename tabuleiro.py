from leitor import dicast
tabuleiro = [[0 for i in range(9)] for i in range(9)]

for lin, col, val in dicast:  # loop pra preencher o tabuleiro
    tabuleiro[lin][col] = val


# função que verifica se nas dicas tem um mesmo número em uma mesma linha
def validacao_linha(dicastratadas):
    nova_lista = [(tupla[0], tupla[2]) for tupla in dicastratadas]
    if len(nova_lista) != len(set(nova_lista)):
        return False
    return True


# função que verifica se nas dicas tem um mesmo número em uma mesma coluna
def validacao_coluna(dicastratadas):
    lista_nova = [(tupla[1], tupla[2]) for tupla in dicastratadas]
    if len(lista_nova) != len(set(lista_nova)):
        return False
    return True


# função que verifica se há somente um número de valor único em cada bloco 3x3
def validacao_bloco(lin, col):
    linha_base = (lin // 3) * 3
    coluna_base = (col // 3) * 3
    bloco = []

    for i in range(linha_base, linha_base + 3):
        for j in range(coluna_base, coluna_base + 3):
            if tabuleiro[i][j] != 0 and tabuleiro[i][j] in bloco:
                return True  # tem repetido
            bloco.append(tabuleiro[i][j])

    return False  # não tem repetido


erro_de_bloco = False  # útil para a mensagem de erro caso haja repetição
for i in range(9):
    for j in range(9):
        if validacao_bloco(i, j) == True:
            erro_de_bloco = True


# função que imprime o tabuleiro bonitinho
def printar_tabuleiro(tab):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print('-' * 32)  # linha horizontal a cada 3 linhas

        linhaf = ''
        for j in range(9):
            if j % 3 == 0 and j != 0:
                linhaf += ' | '  # linha vertical a cada 3 colunas

            valor = tab[i][j]
            if valor == 0:
                linhaf += ' . '
            else:
                linhaf += f'\033[31m{str(valor):^3}\033[m'

        print(linhaf)


# função que verifica se valor pode ser colocado naquela posição
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


# encontra a próxima posição vazia
def espacos_vazios(tab):
    for i in range(9):
        for j in range(9):
            if tab[i][j] == 0:
                return (i, j)
    return None


# preenche o que for possível sem tentativa
def solucionador_parcial(tab):
    progresso = True

    while progresso:
        progresso = False
        for i in range(9):
            for j in range(9):
                if tab[i][j] == 0:
                    possibilidades = [n for n in range(1, 10) if valido(tab, n, (i, j))]
                    if len(possibilidades) == 1:
                        tab[i][j] = possibilidades[0]
                        progresso = True


# tenta todas as possibilidades com backtracking
def solucionador_completo(tab):
    pos = espacos_vazios(tab)
    if not pos:
        return True  # resolvido

    lin, col = pos
    for num in range(1, 10):
        if valido(tab, num, (lin, col)):
            tab[lin][col] = num

            if solucionador_completo(tab):
                return True

            tab[lin][col] = 0  # volta atrás

    return False


# verifica se o tabuleiro está válido para resolver
tabuleiro_valido = validacao_linha(dicast) and validacao_coluna(dicast) and not erro_de_bloco

if __name__ == "__main__":
    if tabuleiro_valido:
        print("Tabuleiro original:")
        printar_tabuleiro(tabuleiro)

        solucionador_parcial(tabuleiro)
        print("\nApós preenchimento parcial:")
        printar_tabuleiro(tabuleiro)

        if solucionador_completo(tabuleiro):
            print("\nTabuleiro resolvido:")
            printar_tabuleiro(tabuleiro)
        else:
            print("\nNÃO FOI POSSÍVEL RESOLVER O TABULEIRO.")
    elif erro_de_bloco:
        print('AS DICAS CONTÊM NÚMEROS REPETIDOS NO MESMO BLOCO')
    else:
        print('AS DICAS CONTÊM NÚMEROS REPETIDOS NA MESMA LINHA OU COLUNA!')