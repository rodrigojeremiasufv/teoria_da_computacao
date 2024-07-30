#Este arquivo define a função principal
import sys
from arquivo import *
from Automato import *

def processa():
    if len(sys.argv) != 3:
        print("Uso correto: python3 main.py <arquivo_automato.txt> <arquivo_strings.txt>")
        sys.exit(1)

    nome_arquivo_automato = sys.argv[1]
    nome_arquivo_strings = sys.argv[2]

    try:
        automato = cria_automato_de_arquivo(nome_arquivo_automato)
        print("--------------- AUTOMATO CRIADO ----------------")
        print(automato)
        print("\n")
        print("----------------- RESULTADO --------------------")
        resultados = processa_strings_arquivo(nome_arquivo_automato, nome_arquivo_strings)
        for string, resultado in resultados.items():
            # print(f"'{resultado}': {string}")
            print("")
    except Exception as e:
        print(f"Erro ao processar os arquivos: {e}")
        sys.exit(1)
processa()