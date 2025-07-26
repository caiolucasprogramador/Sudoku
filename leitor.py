#cria uma lista linha por linha do arquivo de dicas
def ler_dicas(arquivodicas):

    with open(arquivodicas, "r", encoding="utf-8") as texto:
        linhas = [dica.strip() for dica in texto.readlines()]

    return linhas


#trata os erros de usuario, e transforma em uma tupla para preencher o tabuleiro, item por item da lista.
def tratar_entrada(linha):

    linha = linha.replace(' ','')
    linha = linha.replace('=', ':')
    linha = linha.upper()
    
    if ':' in linha and not linha.split(':')[1].startswith(' '):
        linha = linha.replace(':', ': ')
    
    if ':' not in linha:
        return None

    parte1,valor = linha.split(':')
    

    letra,num = parte1.split(',')
    col = ord(letra) - ord('A')
    lin = int(num)-1
    val = int(valor.strip())

    return lin,col,val


