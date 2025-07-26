from interativo import modo_interativo
from solucionador import modo_solucionador  # Assuma que você criou este arquivo e função
from leitor import ler_dicas, tratar_entrada

def carregar_dicas():
    nome_arquivo = input('Digite o caminho do arquivo de dicas: ')
    linhas = ler_dicas(nome_arquivo)
    dicast = []
    for linha in linhas:
        tratada = tratar_entrada(linha)
        if tratada is not None:
            dicast.append(tratada)
    return dicast

def main():
    while True:
        print("\nEscolha o modo:")
        print("1 - Modo Interativo (jogar manualmente)")
        print("2 - Modo Solucionador (resolver automaticamente)")
        print("0 - Sair")
        escolha = input("Digite sua escolha: ").strip()

        if escolha == '1':
            dicast = carregar_dicas()
            modo_interativo(dicast)  # passe dicast como argumento
        elif escolha == '2':
            dicast = carregar_dicas()
            modo_solucionador(dicast)  # passe dicast como argumento
        elif escolha == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()