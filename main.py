#Caio Lucas de Oliveira Ribeiro - 582128
#Davi Freitas Norões Ellery - 579444
#Daniel Ítalo Sousa Alves - 579858
from interativo import modo_interativo
from solucionador import modo_solucionador 
from batch import modo_batch
from leitor import ler_dicas, tratar_entrada


def carregar_dicas():
    nome_arquivo = input('Digite o caminho do arquivo de dicas (na formatação Sudoku/arquivo.txt): ')
    linhas = ler_dicas(nome_arquivo)
    dicast = []
    for linha in linhas:
        tratada = tratar_entrada(linha)
        if tratada is not None:
            dicast.append(tratada)
    return dicast


def main():
    executando = True
    while executando:
        print("\nEscolha o modo:")
        print("1 - Modo Interativo (jogar manualmente)")
        print("2 - Modo Solucionador (resolver automaticamente)")
        print("3 - Modo Batch (executar jogadas em lote a partir de arquivo)")
        print("0 - Sair")
        escolha = input("Digite sua escolha: ").strip()

        if escolha == '1':
            dicast = carregar_dicas()
            modo_interativo(dicast)
        elif escolha == '2':
            dicast = carregar_dicas()
            modo_solucionador(dicast)
        elif escolha == '3':
            modo_batch()
        elif escolha == '0':
            print("Saindo...")
            executando = False
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()
