#cria uma lista linha por linha do arquivo de dicas
def ler_dicas(arquivodicas):

    with open(arquivodicas, "r", encoding="utf-8") as texto:
        linhas = [dica.strip() for dica in texto.readlines()]

    return linhas


#trata os erros de usuario, e transforma em uma tupla para preencher o tabuleiro, item por item da lista.
def tratar_entrada(linha):
    try:

        linha = linha.replace(' ','')
        linha = linha.replace('=', ':')
        linha = linha.upper()
        
        if ':' in linha and not linha.split(':')[1].startswith(' '):
            linha = linha.replace(':', ': ')
        
        if ':' not in linha:
            return None

        parte1,valor = linha.split(':')
        letra,num = parte1.split(',')
        
        valcol = {'A' : 0, 'B' : 1, 'C' : 2 , 'D' : 3, 'E' : 4 , 'F' : 5 , 'G' : 6, 'H' : 7, 'I' : 8}
        
        if letra not in valcol:
            return None

        col = valcol[letra]
        lin = int(num)-1
        val = int(valor.strip())


        entradasvalidas = [0,1,2,3,4,5,6,7,8]
        
        if col not in entradasvalidas or lin not in entradasvalidas:

            return None
        
        return lin,col,val
    except:
        return None

