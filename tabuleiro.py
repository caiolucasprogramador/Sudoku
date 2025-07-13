from leitor import dicast
tabuleiro = [[0 for i in range(9)] for i in range(9)]

for lin,col,val in dicast:      #loop pra preencher o tabuleiro
    tabuleiro[lin][col] = val 

#função que verifica se nas dicas tem um mesmo número em uma mesma linha
def validacao_linha(dicastratadas):
    nova_lista = [(tupla[0], tupla[2]) for tupla in dicastratadas]
    if len(nova_lista) != len(set(nova_lista)):
        return False
    return True

#função que verifica se nas dicas tem um mesmo número em uma mesma coluna
def validacao_coluna(dicastratadas):
    lista_nova = [(tupla[1], tupla[2]) for tupla in dicastratadas]
    if len(lista_nova) != len(set(lista_nova)):
        return False
    return True

#função que verifica se há somente um número de valor único em cada bloco 3x3
def validacao_bloco(lin, col):
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

erro_de_bloco = False
for i in range(9):
    for j in range(9):
        if validacao_bloco(i,j) == True:
            erro_de_bloco = True




#funçao pra imprimir o tabuleiro bonitinho
def printar_tabuleiro(tab):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print('-' * 32)  # linha horizontal a cada 3 linhas

        linhaf = ''
        for j in range(9):
            if j % 3 == 0 and j != 0:
                linhaf += ' | ' #linha vertical a cada 3 colunas

            valor = tab[i][j]
            if valor == 0:
                linhaf += ' . '
            else:
                linhaf += f'\033[31m{str(valor):^3}\033[m'
        
        print(linhaf)


#printa o tabuleiro somente se as dicas tiverem sem erros
if validacao_linha(dicast) == True and validacao_coluna(dicast) == True and erro_de_bloco == False:
    printar_tabuleiro(tabuleiro)
    
elif erro_de_bloco == True:
    print('AS DICAS CONTÉM NÚMEROS REPETIDOS NO MESMO BLOCO')

else:
    print('AS DICAS CONTÉM NÚMEROS REPETIDOS NA MESMA LINHA OU COLUNA!')
