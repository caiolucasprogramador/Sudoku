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
if validacao_linha(dicast) == True and validacao_coluna(dicast) == True:
    printar_tabuleiro(tabuleiro)
else:
    print('AS DICAS CONTÉM NUMEROS REPETIDOS NA MESMA LINHA OU COLUNA!')
