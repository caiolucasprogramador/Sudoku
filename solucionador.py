from tabuleiro import criar_tabuleiro, printar_tabuleiro
from validadores import tabuleiro_valido

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


# Backtracking para resolver o Sudoku
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

def modo_solucionador(dicast):
    tabuleiro = criar_tabuleiro(dicast)

    if tabuleiro_valido(tabuleiro, dicast):
        print("Tabuleiro original:")
        printar_tabuleiro(tabuleiro, [[0]*9 for _ in range(9)])

        if solucionador_completo(tabuleiro):
            print("\nTabuleiro resolvido:")
            printar_tabuleiro(tabuleiro, [[0]*9 for _ in range(9)])
        else:
            print("\nNão foi possível resolver o tabuleiro.")
    else:
        print("As dicas são inválidas. Corrija-as no arquivo de entrada.")