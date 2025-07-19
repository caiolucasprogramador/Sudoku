#funçao pra imprimir o tabuleiro bonitinho
def printar_tabuleiro(tab,tabcomdicas):
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
            elif tabcomdicas is not None and tabcomdicas[i][j] != 0:
                linhaf += f'\033[31m{str(valor):^3}\033[m' 
            else:
                linhaf += f'{str(valor):^3}'
        
        print(linhaf)
