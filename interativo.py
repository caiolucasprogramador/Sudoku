from leitor import ler_dicas, tratar_entrada
from validadores import validacao_linha, validacao_coluna, validacao_bloco, tabuleiro_completo,validacao_colunai,validacao_linhai,validacao_blocoi
from tabuleiro import printar_tabuleiro
from sys import exit

nome_dicas = input('Digite o caminho do arquivo de dicas: ')

dicas = ler_dicas(nome_dicas) #lista das linhas do txt 

dicast = [] #lista com as linhas do txt tratadas e transformadas em tuplas() 
for e in dicas:
    if tratar_entrada(e) is not None:
        dicast.append(tratar_entrada(e))

if len(dicast) < 1 or len(dicast) > 80: #checa se a quantidade de dicas é válida
    print('Número de pistas inválido.')
    exit()

tabuleiro = [[0 for _ in range(9)] for _ in range(9)] #tabuleiro (matriz 9x9)
for lin, col, val in dicast:
    tabuleiro[lin][col] = val
tab_dicas = [linha[:] for linha in tabuleiro] #cópia do tabuleiro original preenchido apenas com as dicas

def blocos_com_erro(tabuleiro):
    for i in range(9):
        for j in range(9):
            if validacao_bloco(tabuleiro, i, j): 
                return True
    return False

if not validacao_linha(dicast) or not validacao_coluna(dicast) or blocos_com_erro(tabuleiro):
    printar_tabuleiro(tabuleiro,tab_dicas)
    print("As dicas violam as regras do Sudoku.")
    exit()

printar_tabuleiro(tabuleiro,tab_dicas)

def tratar_jogada(linha): #funçao que trata as jogadas do usuário e as transforma em tuplas para serem colocadas no tabuleiro
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
        col = ord(letra) - ord('A')
        lin = int(num) - 1
        val = int(valor.strip())

        jogadas_validas = [0,1,2,3,4,5,6,7,8]
        if col not in jogadas_validas or lin not in jogadas_validas:
            return None
        
        return lin,col,val
    except:
        return None
    

jogo_ativo = True
print('\nDigite sua jogada no formato COL,LIN: VALOR')
while jogo_ativo:                                      #loop para realizar e validar as jogadas
    jogada = input('Jogada: ').strip()
    resultado = tratar_jogada(jogada)

    if resultado is not None: 
        lin,col,val = resultado

        if tab_dicas[lin][col] != 0:
            print('Essa posiçao contém uma dica e nao pode ser alterada.')

        elif tabuleiro[lin][col] != 0:
            print('Essa posiçao ja esta preenchida')
            sobr = input('Deseja sobrescrever o valor?\nS para sobrescrever\nN para manter como está: \n').strip().upper()

            if sobr == 'S':
                tabuleiro[lin][col] = val
                if not validacao_linhai(tabuleiro, lin, col) or not validacao_colunai(tabuleiro, lin, col) or not validacao_blocoi(tabuleiro, lin, col):
                    print('jogada inválida: essa jogada fere as regras do sudoku, jogue novamente: ')
                    tabuleiro[lin][col] = 0
                else:
                    printar_tabuleiro(tabuleiro,tab_dicas)
                    if tabuleiro_completo(tabuleiro):
                        print('Sudoku completado!')
                        jogo_ativo = False
            else:
                print('Jogada cancelada')
        else:
            tabuleiro[lin][col] = val
            if not validacao_linhai(tabuleiro, lin, col) or not validacao_colunai(tabuleiro, lin, col) or not validacao_blocoi(tabuleiro, lin, col):
                print('Jogada inválida: essa jogada fere as regras do sudoku, jogue novamente: ')
                tabuleiro[lin][col] = 0
            else:
                printar_tabuleiro(tabuleiro,tab_dicas)
                if tabuleiro_completo(tabuleiro):
                        print('Sudoku completado!')
                        jogo_ativo = False
    else:
        print('Essa jogada é inválida, tente novamente.') #se a funçao de tratar jogada der None, pede outra jogada 